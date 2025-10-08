<span align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![tests](https://github.com/billwallis/bills-sql-linter/actions/workflows/tests.yaml/badge.svg)](https://github.com/billwallis/bills-sql-linter/actions/workflows/tests.yaml)
[![coverage](coverage.svg)](https://github.com/dbrgn/coverage-badge)
[![GitHub last commit](https://img.shields.io/github/last-commit/billwallis/bills-sql-linter)](https://shields.io/badges/git-hub-last-commit)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/billwallis/bills-sql-linter/main.svg)](https://results.pre-commit.ci/latest/github/billwallis/bills-sql-linter/main)

</span>

---

# Bill's SQL Linter

Personal SQL linter.

Built on the following awesome libraries:

- [SQLGlot](https://github.com/tobymao/sqlglot) for SQL parsing
- [arguably](https://github.com/treykeown/arguably) for the CLI

## Quick start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and then enable [pre-commit](https://pre-commit.com/):

```bash
uv sync --all-groups
pre-commit install --install-hooks
```
