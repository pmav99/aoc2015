import pytest

from .part1 import compute


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ["(())", 0],
        ["()()", 0],
        ["(((", 3],
        ["(()(()(", 3],
        ["))(((((", 3],
        ["())", -1],
        ["))(", -1],
        [")))", -3],
        [")())())", -3],
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected
