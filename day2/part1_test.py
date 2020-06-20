from typing import List

import pytest

from . import part1


@pytest.mark.parametrize(
    ("input_s", "expected"), (["2x3x4", 58], ["1x1x10", 43],),
)
def test_compute_one(input_s: str, expected: int) -> None:
    assert part1.compute_one(input_s) == expected


@pytest.mark.parametrize(("lines", "expected"), [(["2x3x4", "1x1x10"], 101)])
def test_compute(lines: List[str], expected: int) -> None:
    assert part1.compute(lines) == expected
