from __future__ import annotations

import dataclasses
import pathlib

import pytest

from bills_sql_linter import fixer

HERE = pathlib.Path(__file__).parent
FIXTURES = HERE / "fixtures"


@dataclasses.dataclass
class BeforeAndAfterFile:
    """
    File contents before and after the fix command is run.
    """

    before: str
    after: str

    @classmethod
    def from_fixture(cls, fixture_name: str) -> BeforeAndAfterFile:
        """
        Return a ``BeforeAndAfterFile`` instance from a fixture name.
        """

        before = FIXTURES / f"{fixture_name}__before.sql"
        after = FIXTURES / f"{fixture_name}__after.sql"

        return cls(
            before=before.read_text(encoding="utf-8"),
            after=after.read_text(encoding="utf-8"),
        )


@pytest.fixture
def simple() -> BeforeAndAfterFile:
    """
    A simple SQL file.
    """

    return BeforeAndAfterFile.from_fixture("simple")


@pytest.mark.skip("Fix isn't built yet")
def test__fix_a_simple_file(simple: BeforeAndAfterFile) -> None:
    assert fixer.fix(simple.before) == simple.after
