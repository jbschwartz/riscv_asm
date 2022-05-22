import enum


class TokenType(enum.Enum):
    SYMBOL = enum.auto()


class Token:
    def __init__(self) -> None:
        self.type = None
