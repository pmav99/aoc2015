import argparse
import sys

from utils import Timer


def compute(text: str) -> int:
    return len(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", default="input.txt")
    args = parser.parse_args()

    with open(args.data_file) as fd:
        text = fd.read().strip()

    with Timer():
        print(compute(text))

    return 0


if __name__ == "__main__":
    sys.exit(main())
