"""--- Day 9: Encoding Error ---"""

from typing import List, Tuple

import pathlib


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]


test = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]


def is_valid(target: int, preamble: List[int]) -> bool:
    results = []
    for num_1 in preamble:
        for num_2 in preamble:
            results.append((num_1 + num_2) == target)
    return any(results)


def find_invalid(preamble_len: int, xmas: List[int]) -> int:
    start = 0
    stop = preamble_len
    size = len(xmas)
    while stop < size:
        preamble = xmas[start:stop]
        target = xmas[stop]
        valid = is_valid(target, preamble)
        if not valid:
            return target
        start = start + 1
        stop = stop + 1


def part_1(preamble_len: int, lines: str) -> int:
    xmas = [int(line) for line in lines]
    return find_invalid(preamble_len, xmas)


def part_2(preamble_len: int, lines: str) -> int:
    xmas = [int(line) for line in lines]
    invalid = find_invalid(preamble_len, xmas)
    start = 0
    stop = 1
    found = None
    size = len(xmas)
    while found is None and start < (size - 1):
        seq = xmas[start:stop]
        if sum(seq) == invalid:
            return min(seq) + max(seq)
        if stop == (size - 1):
            start = start + 1
            stop = start + 1
        else:
            stop = stop + 1


if __name__ == "__main__":
    print(part_1(5, test))
    i = read_input()
    print(part_1(25, i))
    print(part_2(5, test))
    print(part_2(25, i))
