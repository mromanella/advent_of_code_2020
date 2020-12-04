"""
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers);
start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position
that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?


--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes,
you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively;
multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""


from os import read
import pathlib
from typing import List, Tuple

TREE = '#'
CLEAR = '.'

test_1 = [
    '..##.........##.........##.........##.........##.........##.......',
    '#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..',
    '.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.',
    '..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#',
    '.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.',
    '..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....',
    '.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#',
    '.#........#.#........#.#........#.#........#.#........#.#........#',
    '#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...',
    '#...##....##...##....##...##....##...##....##...##....##...##....#',
    '.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#'
]


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]


def is_tree(char: str) -> bool:
    return char == TREE


def part_1(lines: List[str], slope: Tuple[int, int]) -> int:
    count = 0
    x = 0
    y = 0
    x_max = len(lines[0])
    y_max = len(lines)
    while True:
        char = lines[y][x]
        if is_tree(char):
            count += 1
        x = x + slope[0]
        y = y + slope[1]
        if x >= x_max:
            x = x - x_max
        if y >= y_max:
            return count


def mult(values: List[int]) -> int:
    num = values[0]
    for val in values[1:]:
        num *= val
    return num


def part_2(lines: List[str], slopes: List[Tuple[int, int]]) -> int:
    collisions = []
    for slope in slopes:
        collisions.append(part_1(lines, slope))
    num = mult(collisions)
    return num


if __name__ == '__main__':
    print(part_1(test_1, (3, 1)))

    lines = read_input()
    print(part_1(lines, (3, 1)))

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    print(part_2(test_1, slopes))
    print(part_2(lines, slopes))
