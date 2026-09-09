import argparse
import csv
import io
import pathlib
import re
from collections.abc import Sequence

SUCCESS = 0
FAILURE = 1
SELECT_STAR_PATTERN = re.compile(
    r"^ *select +([^\n,]+,[^\n]+)$",
)


def _parse_csv(csv_string: str) -> list[str]:
    csv_io = io.StringIO(csv_string)
    parsed = csv.reader(
        csv_io,
        quoting=csv.QUOTE_NONE,  # type: ignore
    )

    return [c.strip() for c in next(parsed)]


def _format_file(target_path: pathlib.Path) -> None:
    lines = []
    for line in target_path.read_text().split("\n"):
        if match := SELECT_STAR_PATTERN.match(line):
            columns = match.group(1)
            formatted = ",\n".join(_parse_csv(columns))
            line = line.replace(columns, "\n" + formatted)  # noqa: PLW2901
        lines.append(line)

    target_path.write_text("\n".join(lines))


def _lint(args: argparse.Namespace) -> int:
    raise NotImplementedError()


def _format(args: argparse.Namespace) -> int:
    for filename in args.filenames:
        _format_file(target_path=pathlib.Path(filename).resolve())

    return SUCCESS


def main(argv: Sequence[str] | None = None) -> int:
    """
    Parse the arguments and run the command.
    """

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    parser__lint = subparsers.add_parser("lint")
    parser__lint.add_argument("filenames", nargs="*")
    parser__format = subparsers.add_parser("format")
    parser__format.add_argument("filenames", nargs="*")

    args = parser.parse_args(argv)
    if args.command == "lint":
        return _lint(args)
    if args.command == "format":
        return _format(args)

    parser.print_help()
    return SUCCESS


if __name__ == "__main__":
    raise SystemExit(main())  # pragma: no cover
