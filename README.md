# Slack Search Agent

A lightweight Python CLI tool to validate Slack API credentials and run basic Slack searches.

## Quick start

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

3. Configure your bot token:

```bash
cp .env.example .env
# then edit .env and set SLACK_BOT_TOKEN=xoxb-...
```

4. Verify setup:

```bash
python3 test_setup.py
```

5. Run the CLI:

```bash
python3 example.py
```

## Required OAuth scopes

At minimum, configure these scopes for your Slack app:

- `search:read`
- `channels:history`
- `channels:read`
- `users:read`

## Notes

- Keep your token private.
- If `.env` is missing or token is blank, the CLI prompts you to paste a token at runtime.
