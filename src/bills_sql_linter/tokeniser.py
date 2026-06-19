import dataclasses
import enum
import re
from collections.abc import Generator


class TokenType(enum.StrEnum):
    # Literals
    NUMBER = r"\d+(\.\d*)?"
    STRING = r"'[\s\S]*'"  # what about escaped quotes?

    # Operators
    STAR = r"\*"
    PLUS = r"\+"
    MINUS = r"\-"
    DIVIDE = r"\/"

    # Keywords
    AS = r"as"
    SELECT = r"select"
    FROM = r"from"
    IDENTIFIER = r"[a-z_][0-9a-z_]*"
    ESCAPED_IDENTIFIER = r"\\[a-z]"

    # Punctuation
    COMMA = r","
    SEMICOLON = r";"
    SPACE = r"[ \t]+"
    NEWLINE = r"\n"

    @classmethod
    def token_regex(cls) -> re.Pattern:
        pattern = (
            "|".join(f"(?P<{e.name}>{e.value})" for e in cls)
            + "|(?P<UNMATCHED>.)"
        )
        return re.compile(pattern, flags=re.IGNORECASE)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}.{self.name}"


@dataclasses.dataclass
class Token:
    type: TokenType
    value: float | str
    line: int
    column: int


def tokenise(sql: str) -> Generator[Token]:
    """
    Tokeniser, following the MWE at:

    - https://docs.python.org/3/library/re.html#writing-a-tokenizer
    """

    line_num = 1
    line_start = 0
    for match in re.finditer(TokenType.token_regex(), sql):
        value = match.group()
        column = match.start() - line_start
        try:
            token_type = TokenType[match.lastgroup]  # type: ignore  # TODO: Fix typing
        except KeyError:
            err = f"unexpected {value!r} on line {line_num}, position {column}"
            raise NotImplementedError(err) from None

        if token_type == TokenType.NUMBER:
            value = float(value) if "." in value else int(value)
        elif token_type == TokenType.NEWLINE:
            yield Token(token_type, value, line_num, column)
            line_start = match.end()
            line_num += 1
            continue

        yield Token(token_type, value, line_num, column)
