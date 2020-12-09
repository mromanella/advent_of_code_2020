"""--- Day 7: Handy Haversacks ---"""

import pathlib
from collections import namedtuple
from typing import List, Tuple
import networkx as nx
import pylab as plt

test = [
'light red bags contain 1 bright white bag, 2 muted yellow bags.',
'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
'bright white bags contain 1 shiny gold bag.',
'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
'faded blue bags contain no other bags.',
'dotted black bags contain no other bags.'
]

Src = namedtuple('Src', ['name', 'dests'])
Dest = namedtuple('Dest', ['name', 'num'])

def read_input() -> List[str]:
    filepath = pathlib.Path(__file__).parent / 'input.txt'
    with open(filepath, 'r') as infile:
        return [line.rstrip('\n') for line in infile]


def parse_line(line: str) -> Tuple[str, List[Tuple[str, int]]]:
    first, *rest = line.split(',')
    first = first.split(' ')
    src = ' '.join(first[:2])
    if 'no other bags' in line:
        return Src(src, [])
    num = int(first[-4])
    dest = ' '.join(first[-3:-1])
    dests = [Dest(dest, num)]
    for part in rest:
        part = part.split(' ')
        num = int(part[-4])
        dest = ' '.join(part[-3:-1])
        dests.append(Dest(dest, num))
    return Src(src, dests)

def parse_lines(lines: List[str]) -> List[Tuple[str, List[Tuple[str, int]]]]:
    return [parse_line(line) for line in lines]

def create_graph(lines: List[str]) -> nx.DiGraph:
    g = nx.DiGraph()
    paths = parse_lines(lines)
    for path in paths:
        dests = path.dests
        g.add_node(path.name)
        for dest in dests:
            g.add_node(dest.name, num=dest.num)
            g.add_edge(path.name, dest.name)
    return g

def part_1(lines: List[str]) -> int:
    g = create_graph(lines)
    successors = nx.nodes(nx.dfs_tree(g, 'shiny gold'))
    names = set(successors)
    names.remove('shiny gold')
    return len(names)

if __name__ == '__main__':
    print(part_1(test))
    i = read_input()
    g = create_graph(i)
    print(part_1(i))
    nx.draw(g, with_labels=True)
    plt.show()
