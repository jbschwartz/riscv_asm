from .token import Token


class Lexer:
    """A lexer for tokenizing an assembly language input."""

    def __init__(self) -> None:
        pass

    def tokenize(self, string: str) -> list[Token]:
        """Return a list of Tokens from an input string."""
        return [Token() for i in range(6)]
