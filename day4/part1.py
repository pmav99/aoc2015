import hashlib
import sys

from utils import Timer


def compute(secret_key: bytes, no_zeroes: int) -> int:
    exit_condition = "0" * no_zeroes
    number = 1
    while True:
        key = secret_key + f"{number}".encode("utf-8")
        hexdigest = hashlib.md5(key).hexdigest()
        if hexdigest.startswith(exit_condition):
            break
        number += 1
    return number


def main() -> int:
    # part 1
    with Timer():
        print(compute(b"yzbqklnj", no_zeroes=5))

    # part 2
    with Timer():
        print(compute(b"yzbqklnj", no_zeroes=6))

    return 0


if __name__ == "__main__":
    sys.exit(main())
