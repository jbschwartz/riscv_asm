import unittest

from riscv_asm import Lexer, Token, TokenType


class TestLexer(unittest.TestCase):
    def setUp(self) -> None:
        self.lexer = Lexer()

    def test_tokenize_returns_a_list_of_tokens(self) -> None:
        tokens = self.lexer.tokenize("add x9, x20, x21")

        self.assertEqual(len(tokens), 6)
        self.assertTrue(all([isinstance(t, Token) for t in tokens]))

        self.assertEqual(tokens[0].type, TokenType.SYMBOL)
