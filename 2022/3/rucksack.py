import sys
from typing import List, Set, Tuple


data = [x for x in open(sys.argv[1], "r").read().split("\n") if x]


def parse(text: str) -> Set[int]:
    return set([(ord(x.upper()) - 64) + (26 if x.isupper() else 0) for x in list(text)])


def chunk(array: List, step: int = 3) -> List[List]:
    return [array[x : x + step] for x in range(0, len(array), step)]


def parse_part_1(line: str) -> Tuple[Set[int], Set[int]]:
    set_0 = parse(line[: len(line) // 2])
    set_1 = parse(line[len(line) // 2 :])
    return (set_0, set_1)


def parse_part_2(lines: List[str]):
    return tuple(parse(x) for x in lines)


sacks = [parse_part_1(x) for x in data]
priorities = [(x.intersection(y)).pop() for x, y in sacks]
# sum of priorities of duplicated items
print(f"part one: {sum(priorities)}")

groups = [parse_part_2(x) for x in chunk(data)]
items = [x.intersection(y).intersection(z).pop() for x, y, z in groups]
# sum of priorities of triplicated items
print(f"part two: {sum(items)}")
