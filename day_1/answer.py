"""

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. 
Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a 
starfish coin they had left over from a past vacation. They offer you a second one if 
you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. 
Multiplying them together produces the answer, 241861950.

"""

import pathlib
from typing import List, Tuple

test_1 = [1721, 979, 366, 299, 675, 1456]

def readlines(filepath: str) -> List[str]:
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]

def sum_to_2020_2(l: List[int]) -> Tuple[int, int]:
    for i, num_1 in enumerate(l):
        for k, num_2 in enumerate(l):
            if i != k and (num_1 + num_2 == 2020):
                return l[i], l[k]
    return 0, 0


def sum_to_2020_3(l: List[int]) -> Tuple[int, int]:
    for i, num_1 in enumerate(l):
        for k, num_2 in enumerate(l):
            for j, num_3 in enumerate(l):
                if (num_1 + num_2 + num_3) == 2020:
                    return l[i], l[k], l[j]
    return 0, 0, 0


def mult_2(x: int, y: int) -> int:
    return x * y

def mult_3(x: int, y: int, z: int) -> int:
    return x * y * z

def run_test_1():
    x, y = sum_to_2020_2(test_1)
    print(mult_2(x, y))

def run_test_2():
    x, y, z = sum_to_2020_3(test_1)
    print(mult_3(x, y, z))

if __name__ == '__main__':
    run_test_1()
    nums = [int(line) for line in readlines(pathlib.Path(__file__).parent / 'input.txt')]
    x, y = sum_to_2020_2(nums)
    print(x, y, mult_2(x, y))
    run_test_2()
    x, y, z = sum_to_2020_3(nums)
    print(x, y, z, mult_3(x, y, z))
