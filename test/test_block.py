import pytest

from riscv_asm import Block, Token, TokenType

data = (
    (
        Block(" add x9, x20, x21 "),
        [
            Token("add"),
            Token("x9"),
            Token(","),
            Token("x20"),
            Token(","),
            Token("x21"),
        ],
    ),
    (
        Block(".labelName addi x1, x0, +21"),
        [
            Token("."),
            Token("labelName"),
            Token("addi"),
            Token("x1"),
            Token(","),
            Token("x0"),
            Token(","),
            Token("+"),
            Token("21"),
        ],
    ),
    (
        Block("sb x3, -0x4(x2) # A comment to end the line, perhaps."),
        [
            Token("sb"),
            Token("x3"),
            Token(","),
            Token("-"),
            Token("0x4"),
            Token("("),
            Token("x2"),
            Token(")"),
        ],
    ),
    (
        Block("li a0, CONSTANT"),
        [
            Token("li"),
            Token("a0"),
            Token(","),
            Token("CONSTANT"),
        ],
    ),
    (
        Block("# A comment to start the line, perhaps."),
        [],
    ),
    (
        Block(""),
        [],
    ),
)


@pytest.mark.parametrize("block,expected_tokens", data, ids=[case[0].string for case in data])
def test_tokenize_returns_a_list_of_tokens_for_a_valid_instruction(block, expected_tokens) -> None:
    assert len(block.tokens) == len(expected_tokens), "The wrong number of tokens was returned"
    assert all([isinstance(t, Token) for t in block.tokens]), "A token is the wrong Python type"

    assert [t.type for t in block.tokens] == [
        t.type for t in expected_tokens
    ], "A token is the wrong type"

    assert [t.value for t in block.tokens] == [
        t.value for t in expected_tokens
    ], "A token is the wrong type"


def test_tokenize_raises_for_an_unknown_character() -> None:
    block = Block("add $x9, x20, x21")
    with pytest.raises(ValueError):
        _ = block.tokens
