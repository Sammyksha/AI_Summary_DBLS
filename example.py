from __future__ import annotations

from slack_sdk.errors import SlackApiError

from slack_agent import SlackAgent, format_slack_error


def print_menu() -> None:
    print("\nSlack Search Agent")
    print("1) Verify token (auth.test)")
    print("2) List public channels")
    print("3) Search messages")
    print("4) Exit")


def main() -> None:
    agent = SlackAgent.from_env_or_prompt()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                info = agent.auth_test()
                print(f"✅ Authenticated as: {info.get('user')} in workspace {info.get('team')}")
            elif choice == "2":
                limit = int(input("How many channels to fetch? [20]: ").strip() or "20")
                channels = agent.list_public_channels(limit=limit)
                if not channels:
                    print("No channels found.")
                for c in channels:
                    print(f"- #{c.get('name')} ({c.get('id')})")
            elif choice == "3":
                query = input("Search query: ").strip()
                limit = int(input("How many results? [10]: ").strip() or "10")
                results = agent.search_messages(query=query, limit=limit)
                if not results:
                    print("No matching messages found.")
                for r in results:
                    username = r.get("username") or r.get("user") or "unknown"
                    channel = r.get("channel", {}).get("name", "unknown")
                    text = (r.get("text") or "").replace("\n", " ")
                    print(f"- [{channel}] {username}: {text[:160]}")
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Enter 1, 2, 3, or 4.")
        except ValueError:
            print("Please enter a valid number.")
        except SlackApiError as err:
            print(f"❌ {format_slack_error(err)}")


if __name__ == "__main__":
    main()
