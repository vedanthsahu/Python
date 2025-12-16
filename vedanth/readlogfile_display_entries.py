from collections import deque


def view_recent_logs(log_file: str = "bank_log.txt", limit: int = 3) -> None:
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            recent = deque(f, maxlen=limit)

    except FileNotFoundError:
        print("Log file not found. No logs to show yet.")
        return

    except PermissionError:
        print("Permission denied while accessing the log file.")
        return

    except UnicodeDecodeError:
        print("Log file is not a valid UTF-8 text file.")
        return

    if not recent:
        print("No transactions recorded yet.")
        return

    print("\nRecent Transactions:\n")
    for entry in recent:
        print(entry.rstrip())


view_recent_logs()
