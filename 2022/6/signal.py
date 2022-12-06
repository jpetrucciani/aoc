import sys


data = [x for x in open(sys.argv[1], "r").read().split("\n") if x]


def scan(signal: str, length: int = 4) -> int:
    for x in range(0, len(list(signal)) - length):
        chars = set(signal[x : x + length])
        if len(chars) == length:
            return x + length
    return -1


# part one!
print("part one:")
for x in data:
    print(f"scanning '{x}': {scan(x)}")


# part two!
print("part two:")
for x in data:
    print(f"scanning '{x}': {scan(x, length=14)}")
