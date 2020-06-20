from typing import List

import pytest

from . import part2


@pytest.mark.parametrize(
    ("input_s", "expected"), (["2x3x4", 34], ["1x1x10", 14],),
)
def test_compute_one(input_s: str, expected: int) -> None:
    assert part2.compute_one(input_s) == expected


@pytest.mark.parametrize(("lines", "expected"), [(["2x3x4", "1x1x10"], 48)])
def test_compute(lines: List[str], expected: int) -> None:
    assert part2.compute(lines) == expected
