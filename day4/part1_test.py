import pytest

from . import part1


@pytest.mark.parametrize(
    ("input_s", "no_zeroes", "expected"), ((b"abcdef", 5, 609043), (b"pqrstuv", 5, 1048970)),
)
def test_compute(input_s: bytes, no_zeroes: int, expected: int) -> None:
    assert part1.compute(input_s, no_zeroes) == expected
