import copy
import sys
from typing import Dict, List, Tuple


data = [x for x in open(sys.argv[1], "r").read().split("\n\n") if x]


def chunk(array: str, step: int = 4) -> List[str]:
    return [array[x : x + step] for x in range(0, len(array), step)]


def parse_stack(line: str) -> List[str]:
    def _clean(text: str) -> str:
        return "".join([x for x in text if x.isalpha()])

    chunked = chunk(line)
    return [_clean(x) for x in chunked]


def parse_move(line: str) -> Tuple[int, int, int]:
    return tuple(int(x) for x in line.split(" ") if x.isnumeric())


_stacks = data[0].split("\n")
_boxes = [parse_stack(x) for x in _stacks[:-1]]
_indexes = [int(x) for x in _stacks[-1].strip().split(" ") if x]
stacks: Dict[int, List] = {x: [] for x in _indexes}

for layer in reversed(_boxes):
    for i, crate in enumerate(layer):
        stack = _indexes[i]
        if crate:
            stacks[stack].append(crate)

moves = [parse_move(x) for x in data[1].split("\n") if x]


def move(stk: Dict[int, List], moves: List, ordered: bool = False) -> Dict[int, List]:
    stks = copy.deepcopy(stk)
    for move in moves:
        temp: List = []
        times, f, t = move
        for _ in range(times):
            (temp if ordered else stks[t]).append(stks[f].pop())
        while temp:
            stks[t].append(temp.pop())
    return stks


moved_9000 = move(stacks, moves)
tops = [moved_9000[x][-1] for x in _indexes]
print(f"part one: {''.join(tops)}")

moved_9001 = move(stacks, moves, ordered=True)
tops_2 = [moved_9001[x][-1] for x in _indexes]
print(f"part one: {''.join(tops_2)}")
