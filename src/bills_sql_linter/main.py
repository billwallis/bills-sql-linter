from __future__ import annotations

import argparse
import importlib.metadata
import pathlib
from collections.abc import Sequence

from bills_sql_linter import fixer, linter

SUCCESS = 0
FAILURE = 1


def _get_version() -> str:
    return f"%(prog)s {importlib.metadata.version('bills-sql-linter')}"


def _add_common_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("filenames", nargs="*")


def _fix(args: argparse.Namespace) -> int:
    for filename in args.filenames:
        file = pathlib.Path(filename)
        sql = file.read_text(encoding="utf-8")
        file.write_text(fixer.fix(sql), encoding="utf-8")

    return SUCCESS


def _lint(args: argparse.Namespace) -> int:
    for filename in args.filenames:
        file = pathlib.Path(filename)
        sql = file.read_text(encoding="utf-8")
        results = linter.lint(sql)
        print(results)

    return SUCCESS


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the hook.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=_get_version(),
    )

    subparsers = parser.add_subparsers(dest="command")

    parser__fix = subparsers.add_parser("fix")
    _add_common_options(parser__fix)

    parser__lint = subparsers.add_parser("lint")
    _add_common_options(parser__lint)

    args = parser.parse_args(argv)
    if args.command == "fix":
        return _fix(args)
    if args.command == "lint":
        return _lint(args)

    parser.print_help()
    return SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
