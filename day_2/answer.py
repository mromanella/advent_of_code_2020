"""
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates
the lowest and highest number of times a given letter must appear for the password to be valid.
 For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no 
instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, 
both within the limits of their respective policies.

How many passwords are valid according to their policies?


------------------------

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what 
the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy
 rules from his old job at the sled rental place down the street! The Official Toboggan Corporate 
 Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first 
character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies 
have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?

"""

import pathlib
from typing import List, Tuple

from collections import namedtuple, Counter

Policy = namedtuple('Policy', ['min', 'max', 'letter'])

test_1 = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]

def readlines(filepath: str) -> List[str]:
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]

def split_policy_and_password(line: str) -> Tuple[Policy, str]:
    policy, password = line.split(': ')
    range_, letter = policy.split(' ')
    min_allowed, max_allowed = range_.split('-')
    return Policy(int(min_allowed), int(max_allowed), letter), password

def validate_policy_1(line: str) -> bool:
    policy, password = split_policy_and_password(line)
    counts = Counter(password)
    num = counts.get(policy.letter, 0)
    if num < policy.min or num > policy.max:
        return False
    return True

def validate_policy_2(line: str) -> bool:
    offset = -1
    policy, password = split_policy_and_password(line)
    pos_1 = password[policy.min + offset] == policy.letter
    pos_2 = password[policy.max + offset] == policy.letter
    matches = [pos_1, pos_2]
    return matches.count(True) == 1

def part_1(lines: List[str]) -> Tuple[bool, bool]:
    validity = []
    for line in lines:
        validity.append(validate_policy_1(line))
    return validity.count(True), validity.count(False)


def part_2(lines: List[str]) -> Tuple[bool, bool]:
    validity = []
    for line in lines:
        validity.append(validate_policy_2(line))
    return validity.count(True), validity.count(False)

if __name__ == '__main__':
    print(part_1(test_1))

    lines = readlines(pathlib.Path(__file__).parent / 'input.txt')
    print(part_1(lines))

    print(part_2(test_1))
    print(part_2(lines))
