import pytest

from . import part1


@pytest.mark.parametrize(
    ("input_s", "expected"), ((">", 2), ("^>v<", 4), ("^v^v^v^v^v^v", 2),),
)
def test_compute(input_s: str, expected: int) -> None:
    assert part1.compute(input_s) == expected
