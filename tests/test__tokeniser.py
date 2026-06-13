import pytest

from bills_sql_linter import tokeniser


@pytest.mark.parametrize(
    "token_type, expected",
    [
        (tokeniser.TokenType.SELECT, "TokenType.SELECT"),
        (tokeniser.TokenType.IDENTIFIER, "TokenType.IDENTIFIER"),
    ],
)
def test__token_type__has_simple_repr(
    token_type: tokeniser.TokenType,
    expected: str,
):
    assert repr(token_type) == expected


# fmt: off
@pytest.mark.parametrize(
    "sql, expected",
    [
        (
            "select * from foo",
            [
                tokeniser.Token(type=tokeniser.TokenType.SELECT, value='select', line=1, column=0),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=6),
                tokeniser.Token(type=tokeniser.TokenType.STAR, value='*', line=1, column=7),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=8),
                tokeniser.Token(type=tokeniser.TokenType.FROM, value='from', line=1, column=9),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=13),
                tokeniser.Token(type=tokeniser.TokenType.IDENTIFIER, value='foo', line=1, column=14),
            ],
        ),
        (
            "select 123 as id, 45.67 as cost, 'thing' as _p\nfrom foo",
            [
                tokeniser.Token(type=tokeniser.TokenType.SELECT, value='select', line=1, column=0),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=6),
                tokeniser.Token(type=tokeniser.TokenType.NUMBER, value=123, line=1, column=7),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=10),
                tokeniser.Token(type=tokeniser.TokenType.AS, value='as', line=1, column=11),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=13),
                tokeniser.Token(type=tokeniser.TokenType.IDENTIFIER, value='id', line=1, column=14),
                tokeniser.Token(type=tokeniser.TokenType.COMMA, value=',', line=1, column=16),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=17),
                tokeniser.Token(type=tokeniser.TokenType.NUMBER, value=45.67, line=1, column=18),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=23),
                tokeniser.Token(type=tokeniser.TokenType.AS, value='as', line=1, column=24),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=26),
                tokeniser.Token(type=tokeniser.TokenType.IDENTIFIER, value='cost', line=1, column=27),
                tokeniser.Token(type=tokeniser.TokenType.COMMA, value=',', line=1, column=31),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=32),
                tokeniser.Token(type=tokeniser.TokenType.SINGLE_QUOTE, value="'", line=1, column=33),
                tokeniser.Token(type=tokeniser.TokenType.IDENTIFIER, value='thing', line=1, column=34),
                tokeniser.Token(type=tokeniser.TokenType.SINGLE_QUOTE, value="'", line=1, column=39),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=40),
                tokeniser.Token(type=tokeniser.TokenType.AS, value='as', line=1, column=41),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=1, column=43),
                tokeniser.Token(type=tokeniser.TokenType.IDENTIFIER, value='_p', line=1, column=44),
                tokeniser.Token(type=tokeniser.TokenType.NEWLINE, value='\n', line=1, column=46),
                tokeniser.Token(type=tokeniser.TokenType.FROM, value='from', line=2, column=0),
                tokeniser.Token(type=tokeniser.TokenType.SPACE, value=' ', line=2, column=4),
                tokeniser.Token(type=tokeniser.TokenType.IDENTIFIER, value='foo', line=2, column=5),
            ],
        ),
    ],
)
def test__tokenise__can_tokenise_statements(
    # How are we gonna handle more complex SQL examples? Outsource to fixtures?
    sql: str,
    expected: list[tokeniser.Token],
):
    assert list(tokeniser.tokenise(sql)) == expected
# fmt: on


def test__tokenise__raises_not_implemented_on_unknown_tokens():
    with pytest.raises(NotImplementedError):
        # Assuming null bytes are a no-no in SQL scripts
        list(tokeniser.tokenise(f"select {chr(0)}"))
