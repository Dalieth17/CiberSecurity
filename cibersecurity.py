"""Resume fallos de autenticación a partir de registros JSON Lines sintéticos."""

import argparse
from collections import Counter
import json
import re
import sys


ACTOR_ID = re.compile(r"actor-[0-9]{1,9}")


def analyze(lines):
    failed_attempts = Counter()
    invalid_lines = 0

    for line in lines:
        try:
            record = json.loads(line.decode("utf-8"))
        except (UnicodeDecodeError, ValueError, RecursionError):
            invalid_lines += 1
            continue

        if not isinstance(record, dict):
            invalid_lines += 1
            continue

        actor = record.get("actor_id")
        outcome = record.get("outcome")
        if (
            not isinstance(actor, str)
            or not ACTOR_ID.fullmatch(actor)
            or outcome not in ("success", "failure")
        ):
            invalid_lines += 1
        elif outcome == "failure":
            failed_attempts[actor] += 1

    return {"failed_attempts": dict(failed_attempts), "invalid_lines": invalid_lines}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", help="archivo local JSON Lines")
    arguments = parser.parse_args()

    try:
        with open(arguments.archivo, "rb") as source:
            report = analyze(source)
    except OSError:
        print("No se pudo leer el archivo de entrada.", file=sys.stderr)
        return 1

    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
