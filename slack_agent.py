from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


@dataclass
class SlackAgent:
    token: str

    def __post_init__(self) -> None:
        self.client = WebClient(token=self.token)

    @classmethod
    def from_env_or_prompt(cls) -> "SlackAgent":
        load_dotenv()
        token = os.getenv("SLACK_BOT_TOKEN", "").strip()
        if not token:
            token = input("Enter your Slack Bot Token (xoxb-...): ").strip()
        return cls(token=token)

    def auth_test(self) -> dict[str, Any]:
        return self.client.auth_test()

    def list_public_channels(self, limit: int = 20) -> list[dict[str, Any]]:
        resp = self.client.conversations_list(limit=limit, types="public_channel")
        return resp.get("channels", [])

    def search_messages(self, query: str, limit: int = 10) -> list[dict[str, Any]]:
        resp = self.client.search_messages(query=query, count=limit, sort="timestamp")
        matches = resp.get("messages", {}).get("matches", [])
        return matches


def format_slack_error(error: SlackApiError) -> str:
    payload = getattr(error.response, "data", {}) if error.response else {}
    code = payload.get("error", "unknown_error")
    needed = payload.get("needed")
    if needed:
        return f"Slack API error: {code} (needed scope: {needed})"
    return f"Slack API error: {code}"
