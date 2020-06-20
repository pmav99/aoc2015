import argparse
import sys

from utils import Timer


def compute(input_s: str) -> int:
    go_up = "("
    index = 0
    current = 0
    for index, char in enumerate(input_s, 1):
        if char == go_up:
            current += 1
        else:
            current -= 1
        if current == -1:
            break
    return index


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as fd:
        input_s = fd.read()

    with Timer():
        print(compute(input_s))

    return 0


if __name__ == "__main__":
    sys.exit(main())
