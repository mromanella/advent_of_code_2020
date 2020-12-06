"""--- Day 6: Custom Customs ---"""

import pathlib
from collections import Counter
from typing import List, Set


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]

test = [
    'abc',
    '\n',
    'a',
    'b',
    'c',
    '\n',
    'ab',
    'ac',
    '\n',
    'a',
    'a',
    'a',
    'a',
    '\n',
    'b'
]

def separate_groups(lines: List[str]) -> List[Set[str]]:
    group = []
    groups = []
    for line in lines:
        if line == '\n' or line == '':
            groups.append(group)
            group = []
        else:
            group.append(set(line))
    groups.append(group)
    return groups

def part_1(lines: List[str]) -> int:
    groups = separate_groups(lines)
    yes_counts = []
    for group in groups:
        yes = set()
        for individual in group:
            yes.update(*individual)
        yes_counts.append(len(yes))
    return sum(yes_counts)


def part_2(lines: List[str]) -> int:
    all_yes_counts = []
    groups = separate_groups(lines)
    for group in groups:
        individual_count = len(group)
        same_yes = group[0]
        if individual_count > 1:
            for individual in group:
                same_yes = same_yes.intersection(individual)
        all_yes_counts.append(len(same_yes))
    return sum(all_yes_counts)

if __name__ == '__main__':
    print(part_1(test))
    puzzle_input = read_input()
    print(part_1(puzzle_input))
    print()
    print(part_2(test))
    print(part_2(puzzle_input))