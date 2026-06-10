#!/usr/bin/env python
"""Manage planner-tester-v1 SUBAGENT_CALL_LOG.md files.

Commands:
  init       Create SUBAGENT_CALL_LOG.md with the standard table header.
  append     Append one role/subagent log row.
  validate   Check that the log exists and has usable rows.
  summarize  Print a compact summary of logged rows.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path
import sys


LOG_FILENAME = "SUBAGENT_CALL_LOG.md"
HEADER = (
    "# Subagent Call Log\n\n"
    "| Time | Phase | Subagent | Purpose | Input Summary | Output Summary | Supervisor Decision |\n"
    "|------|-------|----------|---------|---------------|----------------|---------------------|\n"
)
COLUMNS = [
    "Time",
    "Phase",
    "Subagent",
    "Purpose",
    "Input Summary",
    "Output Summary",
    "Supervisor Decision",
]


def resolve_log_path(project: str | None, log_path: str | None) -> Path:
    if log_path:
        return Path(log_path).expanduser().resolve()
    base = Path(project).expanduser().resolve() if project else Path.cwd().resolve()
    return base / LOG_FILENAME


def escape_cell(value: str) -> str:
    cleaned = " ".join((value or "").split())
    return cleaned.replace("|", "\\|")


def unescape_cell(value: str) -> str:
    return value.strip().replace("\\|", "|")


def split_markdown_row(line: str) -> list[str]:
    body = line.strip().strip("|")
    cells: list[str] = []
    current: list[str] = []
    escaped = False

    for char in body:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            escaped = True
            current.append(char)
            continue
        if char == "|":
            cells.append("".join(current))
            current = []
            continue
        current.append(char)

    cells.append("".join(current))
    return [unescape_cell(cell) for cell in cells]


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def init_log(path: Path, force: bool = False) -> int:
    ensure_parent(path)
    if path.exists() and not force:
        print(f"Log already exists: {path}")
        return 0
    path.write_text(HEADER, encoding="utf-8", newline="\n")
    print(f"Initialized log: {path}")
    return 0


def append_log(args: argparse.Namespace) -> int:
    path = resolve_log_path(args.project, args.log_path)
    if not path.exists():
        init_log(path)

    time_value = args.time or datetime.now().strftime("%Y-%m-%d %H:%M")
    row = [
        time_value,
        args.phase,
        args.subagent,
        args.purpose,
        args.input,
        args.output,
        args.decision,
    ]

    missing = [COLUMNS[i] for i, value in enumerate(row) if not value]
    if missing:
        print(f"Missing required fields: {', '.join(missing)}", file=sys.stderr)
        return 2

    line = "| " + " | ".join(escape_cell(value) for value in row) + " |\n"
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    print(f"Appended log row: {path}")
    return 0


def parse_rows(path: Path) -> list[list[str]]:
    if not path.exists():
        return []

    rows: list[list[str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "------" in stripped:
            continue
        cells = split_markdown_row(stripped)
        if len(cells) != len(COLUMNS):
            continue
        if cells == COLUMNS:
            continue
        rows.append(cells)
    return rows


def validate_log(args: argparse.Namespace) -> int:
    path = resolve_log_path(args.project, args.log_path)
    if not path.exists():
        print(f"Missing log file: {path}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if HEADER.splitlines()[2] not in text:
        errors.append("Missing standard table header.")
    if "TODO" in text:
        errors.append("Log still contains TODO placeholder text.")

    rows = parse_rows(path)
    if not rows:
        errors.append("No log rows found.")

    for index, row in enumerate(rows, start=1):
        missing_cols = [COLUMNS[i] for i, value in enumerate(row) if not value.strip()]
        if missing_cols:
            errors.append(f"Row {index} has empty fields: {', '.join(missing_cols)}.")

    if args.require_gate1:
        has_gate1 = any("gate 1" in " ".join(row).lower() for row in rows)
        if not has_gate1:
            errors.append("Gate 1 entry is required but missing.")

    if args.require_gate2:
        has_gate2 = any("gate 2" in " ".join(row).lower() for row in rows)
        if not has_gate2:
            errors.append("Gate 2 entry is required but missing.")

    if errors:
        print(f"Validation failed: {path}", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validation passed: {path}")
    print(f"Rows: {len(rows)}")
    return 0


def summarize_log(args: argparse.Namespace) -> int:
    path = resolve_log_path(args.project, args.log_path)
    rows = parse_rows(path)
    if not rows:
        print(f"No rows found in: {path}", file=sys.stderr)
        return 1

    print(f"Log: {path}")
    print(f"Rows: {len(rows)}")
    for row in rows:
        time_value, phase, subagent, purpose, _input, _output, decision = row
        print(f"- {time_value} | {phase} | {subagent}: {purpose} -> {decision}")
    return 0


def export_csv(args: argparse.Namespace) -> int:
    path = resolve_log_path(args.project, args.log_path)
    rows = parse_rows(path)
    if not rows:
        print(f"No rows found in: {path}", file=sys.stderr)
        return 1

    output_path = Path(args.output).expanduser().resolve()
    ensure_parent(output_path)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(COLUMNS)
        writer.writerows(rows)
    print(f"Exported CSV: {output_path}")
    return 0


def add_common_path_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--project",
        help=f"Project folder that contains {LOG_FILENAME}. Defaults to current directory.",
    )
    parser.add_argument(
        "--log-path",
        help=f"Explicit path to {LOG_FILENAME}. Overrides --project.",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a log file.")
    add_common_path_args(init_parser)
    init_parser.add_argument("--force", action="store_true", help="Overwrite an existing log.")
    init_parser.set_defaults(func=lambda args: init_log(resolve_log_path(args.project, args.log_path), args.force))

    append_parser = subparsers.add_parser("append", help="Append one log row.")
    add_common_path_args(append_parser)
    append_parser.add_argument("--time", help="Timestamp. Defaults to current local time.")
    append_parser.add_argument("--phase", required=True)
    append_parser.add_argument("--subagent", required=True)
    append_parser.add_argument("--purpose", required=True)
    append_parser.add_argument("--input", required=True)
    append_parser.add_argument("--output", required=True)
    append_parser.add_argument("--decision", required=True)
    append_parser.set_defaults(func=append_log)

    validate_parser = subparsers.add_parser("validate", help="Validate the log file.")
    add_common_path_args(validate_parser)
    validate_parser.add_argument("--require-gate1", action="store_true")
    validate_parser.add_argument("--require-gate2", action="store_true")
    validate_parser.set_defaults(func=validate_log)

    summarize_parser = subparsers.add_parser("summarize", help="Print a short summary.")
    add_common_path_args(summarize_parser)
    summarize_parser.set_defaults(func=summarize_log)

    csv_parser = subparsers.add_parser("export-csv", help="Export the log table to CSV.")
    add_common_path_args(csv_parser)
    csv_parser.add_argument("--output", required=True, help="Destination CSV path.")
    csv_parser.set_defaults(func=export_csv)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
