"""Command-line interface with JSON persistence."""
import argparse
import json
from pathlib import Path
from .tasks import add_task, list_tasks, finish_task


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=Path, default=Path("tasks.json"))
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("add").add_argument("title")
    subs.add_parser("list")
    subs.add_parser("complete").add_argument("task_id", type=int)
    args = parser.parse_args()
    tasks = json.loads(args.file.read_text()) if args.file.exists() else []
    try:
        if args.command == "add":
            result = add_task(tasks, args.title)
        elif args.command == "complete":
            result = finish_task(tasks, args.task_id)
        else:
            result = list_tasks(tasks)
    except (ValueError, KeyError) as error:
        parser.exit(2, f"{error}\n")
    if args.command != "list":
        args.file.write_text(json.dumps(tasks) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
