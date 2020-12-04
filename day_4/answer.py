"""
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as
a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport
is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like
 data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you
 made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but
missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?


--- Part Two ---
The line is moving more quickly now, but you overhear airport security talking about how passports
with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to
the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and valid values. Continue to
treat cid as optional. In your batch file, how many passports are valid?

"""

import pathlib
from typing import Dict, List


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]


test = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '\n',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '\n',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '\n',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in'
]

BYR = 'byr'
IYR = 'iyr'
EYR = 'eyr'
HGT = 'hgt'
HCL = 'hcl'
ECL = 'ecl'
PID = 'pid'
CID = 'cid'

FIELDS = {
    BYR,
    IYR,
    EYR,
    HGT,
    HCL,
    ECL,
    PID,
    CID
}

REQUIRED_FIELDS = {
    BYR,
    IYR,
    EYR,
    HGT,
    HCL,
    ECL,
    PID
}

OPTIONAL_FIELDS = {
    CID
}


def separate_passports(lines: List[str]) -> List[Dict[str, str]]:
    passports = []
    passport = {}
    for line in lines:
        if line == '\n' or line == '':
            passports.append(passport)
            passport = {}
        else:
            fields = line.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport[key] = value
    # Append last line
    passports.append(passport)
    return passports


def validate_byr(value: str) -> bool:
    val = int(value)
    if val < 1920 or val > 2020:
        return False
    return True


def validate_iyr(value: str) -> bool:
    val = int(value)
    if val < 2010 or val > 2020:
        return False
    return True


def validate_eyr(value: str) -> bool:
    val = int(value)
    if val < 2020 or val > 2030:
        return False
    return True


def validate_hgt(value: str) -> bool:
    cm = 'cm'
    inch = 'in'
    if cm in value:
        val = int(value.rstrip(cm))
        if val < 150 or val > 193:
            return False
        return True
    else:
        # Assuming inch
        val = int(value.rstrip(inch))
        if val < 59 or val > 76:
            return False
        return True


def validate_hcl(value: str) -> bool:
    valid = {'0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
    if '#' not in value:
        return False
    if len(value) != 7:
        return False
    for c in value[1:]:
        if c.lower() not in valid:
            return False
    return True


def validate_ecl(value: str) -> bool:
    valid = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    return value in valid


def validate_pid(value: str) -> bool:
    if len(value) == 9:
        try:
            int(value)
        except ValueError:
            return False
        return True
    return False


VALIDATIONS = {
    BYR: validate_byr,
    IYR: validate_iyr,
    EYR: validate_eyr,
    HGT: validate_hgt,
    HCL: validate_hcl,
    ECL: validate_ecl,
    PID: validate_pid
}


def has_required_fields(passport: Dict[str, str]) -> bool:
    keys = set(passport.keys())
    if REQUIRED_FIELDS.intersection(keys) == REQUIRED_FIELDS:
        return True
    return False


def part_1(lines: str) -> int:
    passports = separate_passports(lines)
    valid = 0
    for passport in passports:
        if has_required_fields(passport):
            valid += 1
    return valid


def has_valid_fields(passport: Dict[str, str]) -> bool:
    for key, value in passport.items():
        if key == CID:
            continue
        validate_func = VALIDATIONS[key]
        if not validate_func(value):
            return False
    return True


def part_2(lines: str) -> int:
    passports = separate_passports(lines)
    valid = 0
    for passport in passports:
        if has_required_fields(passport) and has_valid_fields(passport):
            valid += 1
    return valid


test_2 = [
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
    'hcl:#623a2f',
    '\n',
    'eyr:2029 ecl:blu cid:129 byr:1989',
    'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
    '\n',
    'hcl:#888785',
    'hgt:164cm byr:2001 iyr:2015 cid:88',
    'pid:545766238 ecl:hzl',
    'eyr:2022',
    '\n',
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'
]
if __name__ == '__main__':
    print(part_1(test))
    lines = read_input()
    print(part_1(lines))

    print(part_2(test_2))
    print(part_2(lines))
