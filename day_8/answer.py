"""--- Day 8: Handheld Halting ---"""


from typing import List, Tuple

import pathlib


def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]


def accumulator():
    _acc = 0

    def _accumulator(value: int = None):
        nonlocal _acc
        if value is None:
            return _acc
        else:
            _acc += value
            return _acc
    return _accumulator


test = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'


def parse_line(line: str) -> Tuple[str, int]:
    cmd, val = line.split(' ')
    val = int(val)
    return cmd, val


class ProgramRunner:

    def __init__(self, program: List[str]):
        self.program = program
        self.parsed_program = [parse_line(line) for line in self.program]
        self.pc = 0
        self.accumulator = accumulator()
        self.already_run = set()
        self.running = False
        self.ops = {
            ACC: self.accumulate,
            JMP: self.jump,
            NOP: self.nop
        }

    def run(self):
        loop_term = False
        self.running = True
        while self.running and self.pc < len(self.parsed_program):
            if self.pc in self.already_run:
                self.running = False
                loop_term = True
            else:
                self.already_run.add(self.pc)
                cmd, val = self.parsed_program[self.pc]
                op = self.ops[cmd]
                op(val)
        return loop_term

    def accumulate(self, value: int):
        self.accumulator(value)
        self.pc += 1

    def jump(self, value: int) -> int:
        self.pc += value

    def nop(self, value: int):
        self.pc += 1


def part_1(lines: List[str]) -> int:
    runner = ProgramRunner(lines)
    runner.run()
    return runner.accumulator()


def part_2(lines: List[str]) -> int:
    line_num = 0
    loop_term = True
    runner = None
    while line_num < len(lines) and loop_term is True:
        copy = [line for line in lines]
        line = copy[line_num]
        if JMP in line:
            l = line.replace(JMP, NOP)
        elif NOP in line:
            l = line.replace(NOP, JMP)
        else:
            line_num += 1
            continue

        copy[line_num] = l
        runner = ProgramRunner(copy)
        loop_term = runner.run()
        line_num += 1
    return runner.accumulator()


if __name__ == "__main__":
    print(part_1(test))
    i = read_input()
    print(part_1(i))
    print(part_2(test))
    print(part_2(i))
