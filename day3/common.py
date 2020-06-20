import typing


NORTH = "^"
SOUTH = "v"
EAST = ">"
WEST = "<"


def process_step(x: int, y: int, step: str) -> typing.Tuple[int, int]:
    if step == NORTH:
        y += 1
    elif step == SOUTH:
        y -= 1
    elif step == EAST:
        x += 1
    elif step == WEST:
        x -= 1
    else:
        raise ValueError(f"WTF???: {step}")
    return (x, y)
