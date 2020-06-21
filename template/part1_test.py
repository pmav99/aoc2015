import pytest

from . import part1


@pytest.mark.parametrize(
    ("input_s", "expected"), (("input_string1", 2), ("input_string2", 4), ("input_string3", 2)),
)
def test_compute(input_s: str, expected: int) -> None:
    assert part1.compute(input_s) == expected
