from typing import Tuple

Point = Tuple[int, int]
Line = Tuple[Point, Point]


def calc_slope(line: Line) -> (int, int):
    (x1, y1), (x2, y2) = line
    return (x1 - x2), (y1 - y2)

