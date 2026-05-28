#!/usr/bin/env python3

import argparse
import json
import pathlib

from jsonschema import Draft202012Validator


def load_json(path: pathlib.Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_jsonl(path: pathlib.Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            rows.append((idx, json.loads(line)))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schema", required=True)
    parser.add_argument("--dataset", required=True)
    args = parser.parse_args()

    schema = load_json(pathlib.Path(args.schema))
    validator = Draft202012Validator(schema)

    failed = False
    for line_no, row in load_jsonl(pathlib.Path(args.dataset)):
        errors = sorted(validator.iter_errors(row), key=lambda e: list(e.path))
        if errors:
            failed = True
            print(f"Line {line_no} failed:")
            for e in errors:
                path = ".".join(str(p) for p in e.path) if e.path else "$"
                print(f"  - {path}: {e.message}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
