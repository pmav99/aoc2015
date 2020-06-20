import argparse
import sys
from typing import List

from utils import Timer


def compute_one(input_s: str) -> int:
    width, height, length = map(int, input_s.split("x"))
    length_width = length * width
    width_height = width * height
    height_length = height * length
    area = 2 * (length_width + width_height + height_length) + min(length_width, width_height, height_length)
    return area


def compute(lines: List[str]) -> int:
    total = sum(compute_one(line) for line in lines)
    return total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as fd:
        lines = [line.strip() for line in fd.readlines() if line.strip()]

    with Timer():
        print(compute(lines))

    return 0


if __name__ == "__main__":
    sys.exit(main())
