import enum
from typing import Optional


class TokenType(enum.Enum):
    """Type of permissible Tokens in an assembly code Block."""

    ALPHANUM = chr(0)
    CLOSE_PAREN = ")"
    COMMA = ","
    MINUS = "-"
    OPEN_PAREN = "("
    PERIOD = "."
    PLUS = "+"


# pylint: disable=too-few-public-methods
class Token:
    """A single Token found in an assembly code Block."""

    def __init__(self, value: Optional[str] = "") -> None:
        """Create a new Token with the text value."""
        self.value = value

        # Ensure that the token value is a recognizable type. Alphanumeric types will not
        # match the enumeration's value so check them separately.
        try:
            self.type = TokenType(self.value)
        except ValueError as e:
            if self.value is not None and not self.value.isalnum():
                raise e

            self.type = TokenType.ALPHANUM if self.value.isalnum() else None

    def __str__(self) -> str:
        """Return a readable representation of the Token."""
        return f'"{self.value}" ({str(self.type.name)})'
