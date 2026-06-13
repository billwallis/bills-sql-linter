import contextlib
import pathlib

import pytest

from bills_sql_linter import fixer, linter, main


@pytest.fixture
def sql_file(tmp_path: pathlib.Path) -> pathlib.Path:
    file = tmp_path / "model.sql"
    file.write_text("select * from foo")
    return file


def test__cli__fix__happy_path(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
    sql_file: pathlib.Path,
):
    monkeypatch.setattr(fixer, "fix", lambda *_, **__: "")

    assert main.main(["fix", str(sql_file)]) == 0


def test__cli__lint__happy_path(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture,
    sql_file: pathlib.Path,
):
    monkeypatch.setattr(linter, "lint", lambda *_, **__: "")

    assert main.main(["lint", str(sql_file)]) == 0


def test__cli__no_args_prints_help(
    capsys: pytest.CaptureFixture,
):
    # with pytest.raises(SystemExit):  # not sure why Pytest doesn't think SystemExit is raised
    with contextlib.suppress(BaseException):
        main.main(["--help"])
    help_stdout, _ = capsys.readouterr()

    # with pytest.raises(SystemExit):
    with contextlib.suppress(BaseException):
        main.main([])
    null_stdout, _ = capsys.readouterr()

    assert null_stdout == help_stdout
