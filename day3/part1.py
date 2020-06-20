import argparse
import sys

from utils import Timer

from .common import process_step


def compute(steps: str) -> int:
    (x, y) = (0, 0)
    visited = {(x, y)}
    for step in steps:
        x, y = process_step(x, y, step)
        visited.add((x, y))
    return len(visited)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as fd:
        text = fd.read().strip()

    with Timer():
        print(compute(text))

    return 0


if __name__ == "__main__":
    sys.exit(main())
