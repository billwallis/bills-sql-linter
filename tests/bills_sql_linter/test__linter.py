from __future__ import annotations

import pytest

from bills_sql_linter import linter


@pytest.mark.skip("Lint isn't built yet")
def test__lint_a_file() -> None:
    assert linter.lint("select * from foo")
