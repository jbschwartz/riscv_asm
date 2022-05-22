from functools import cached_property
from typing import Optional

from .token import Token, TokenType


class Block:
    """A single line of assembly code.

    This class is used as a lexer for tokenizing the input assembly."""

    def __init__(self, line: str = "") -> None:
        self.string = line
        # Store the index of a cursor for iterating through the string.
        self.cursor = 0

        # It's safe to assume that if a new line ends up in the middle of the string,
        # something is wrong.
        assert (
            self.string.index("\n") == (len(self.string) - 1) if "\n" in self.string else True
        ), "New line character found in the middle of assembly code line"

    @cached_property
    def tokens(self) -> list[Token]:
        """Lex the assembly code and return a list of Tokens found.

        This function returns an empty list if no tokens are found.
        """
        # Just in case the cached property is deleted and recomputed.
        self.cursor = 0

        tokens = []
        while token := self._next_token():
            tokens.append(token)

        return tokens

    @property
    def _char(self) -> Optional[str]:
        """Return the character being read at the current cursor index.

        Return None if the cursor is outside the bounds of the string.
        """
        try:
            return self.string[self.cursor]
        except IndexError:
            return None

    def _comment(self) -> None:
        """Advance the cursor over a comment to the end of the string."""
        if self._char == "#":
            # Skip all the way to the end of the string.
            self.cursor = len(self.string)

    def _consume(self) -> Optional[str]:
        """Return the current character and advance the cursor by one."""
        char = self._char
        self.cursor += 1
        return char

    def _next_token(self) -> Optional[Token]:
        """Return the next Token from the current cursor position."""
        self._whitespace()
        self._comment()

        # n.b. This assumes that non-alphanumerics are all single characters.
        if self._char in [type.value for type in TokenType]:
            return Token(self._consume())

        if self._char and self._char.isalnum():
            string = ""
            while self._char and self._char.isalnum():
                string += self._consume()

            return Token(string) if string else None

        if self._char is not None:
            raise ValueError(f"Unknown character found: '{self._char}' at position {self.cursor}")

    def _whitespace(self) -> None:
        """Advance the cursor over any whitespace characters."""
        while self._char in [" ", "\t", "\r", "\n"]:
            self.cursor += 1
