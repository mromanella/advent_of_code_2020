"""
--- Day 5: Binary Boarding ---

"""

import pathlib
from math import floor, ceil
from typing import List, Tuple

test = [
    'FBFBBFFRLR',
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL'
]

FRONT = 'F'
BACK = 'B'
RIGHT = 'R'
LEFT = 'L'


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]

def split_row_from_column(boarding_pass: str) -> Tuple[str, str]:
    return boarding_pass[:7], boarding_pass[7:]

def converge(regions: str, min_: int, max_: int) -> int:
    for region in regions:
        if region == FRONT or region == LEFT:
            max_ = min_ + ((max_ - min_) // 2)
        elif region == BACK or region == RIGHT:
            min_ = min_ + ceil((max_ - min_) / 2)
    return min_

def determine_row(row_regions: str) -> int:
    return converge(row_regions, 0, 127)

def determine_column(column_regions: str) -> int:
    return converge(column_regions, 0, 7)

def determine_seat_id(boarding_pass: str) -> int:
    row_reg, column_reg = split_row_from_column(boarding_pass)
    row = determine_row(row_reg)
    column = determine_column(column_reg)
    return row * 8 + column

def determine_seat_ids(boarding_passes: List[str]) -> List[int]:
    seat_ids = [determine_seat_id(boarding_pass) for boarding_pass in boarding_passes]
    return seat_ids

def part_1(lines: List[str]) -> int:
    seat_ids = determine_seat_ids(lines)
    return max(seat_ids)

def part_2(lines: List[str]) -> int:
    seat_ids = determine_seat_ids(lines)
    max_seat_id = max(seat_ids)
    seat_ids = set(seat_ids)
    all_seats = set(list(range(0, max_seat_id + 1)))
    missing_ids = all_seats.difference(seat_ids)
    for seat_id in missing_ids:
        one_up = seat_id + 1
        one_down = seat_id - 1
        if one_down in seat_ids and one_up in seat_ids:
            return seat_id

if __name__ == '__main__':
    print(part_1(test))
    boarding_passes = read_input()
    print(part_1(boarding_passes))
    print(part_2(boarding_passes))
