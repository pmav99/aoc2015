import pytest

from . import part2


@pytest.mark.parametrize(
    ("input_s", "expected"), (("^v", 3), ("<>", 3), ("^>v<", 3), ("^v^v^v^v^v", 11)),
)
def test_compute(input_s: str, expected: int) -> None:
    assert part2.compute(input_s) == expected
