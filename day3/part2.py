import argparse
import sys

from utils import Timer

from .common import process_step


def compute(steps: str) -> int:
    (x_normal, y_normal) = (x_robot, y_robot) = (0, 0)
    visited = {(x_normal, y_normal)}
    for i, step in enumerate(steps):
        if i % 2 == 0:
            # normal santa
            x_normal, y_normal = process_step(x_normal, y_normal, step)
            visited.add((x_normal, y_normal))
        else:
            # robot santa
            x_robot, y_robot = process_step(x_robot, y_robot, step)
            visited.add((x_robot, y_robot))
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
