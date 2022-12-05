import sys
from typing import Set, Tuple


data = [x for x in open(sys.argv[1], "r").read().split("\n") if x]


def parse(line: str) -> Tuple[Set, Set]:
    ranges = [x.split("-") for x in line.split(",")]
    set_0, set_1 = [set(range(int(x[0]), int(x[1]) + 1)) for x in ranges]
    return set_0, set_1


assignments = [parse(x) for x in data]
overlaps = [x.issubset(y) or y.issubset(x) for x, y in assignments]
# sum of assignment pairs where one range fully contains the other
print(f"part one: {sum(overlaps)}")

all_overlaps = [bool(x.intersection(y)) for x, y in assignments]
# sum of assignment pairs where any overlap occurs
print(f"part one: {sum(all_overlaps)}")
