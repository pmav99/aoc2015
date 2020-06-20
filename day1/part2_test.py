import pytest

from .part2 import compute


@pytest.mark.parametrize(
    ("input_s", "expected"), ([")", 1], ["()())", 5], ["((())))", 7],),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
