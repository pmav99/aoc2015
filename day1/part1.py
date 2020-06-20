import argparse
import sys

from utils import Timer


def compute(input_s: str) -> int:
    opening = input_s.count("(")
    # closing = input_s.count(")")
    closing = len(input_s) - opening
    return opening - closing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file")
    args = parser.parse_args()

    with open(args.data_file) as fd:
        input_s = fd.read().strip()

    with Timer():
        print(compute(input_s))

    return 0


if __name__ == "__main__":
    sys.exit(main())
