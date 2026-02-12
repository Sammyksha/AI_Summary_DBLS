from __future__ import annotations

import os
import sys

from dotenv import load_dotenv


def check_imports() -> bool:
    try:
        import slack_sdk  # noqa: F401
        import yaml  # noqa: F401
        print("✅ Python dependencies import correctly")
        return True
    except Exception as err:  # pragma: no cover - sanity script
        print(f"❌ Dependency import failed: {err}")
        return False


def check_token() -> bool:
    load_dotenv()
    token = os.getenv("SLACK_BOT_TOKEN", "").strip()
    if token.startswith("xoxb-"):
        print("✅ SLACK_BOT_TOKEN looks valid (xoxb-...) in .env")
        return True
    print("⚠️ SLACK_BOT_TOKEN not set in .env (or does not start with xoxb-)")
    return False


def main() -> None:
    ok_imports = check_imports()
    _ = check_token()

    if not ok_imports:
        sys.exit(1)

    print("\nSetup check complete.")


if __name__ == "__main__":
    main()
