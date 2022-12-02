import sys

data = open(sys.argv[1], "r").read()
groups = data.split("\n\n")
values = [list(map(int, x.strip().split("\n"))) for x in groups]
elves = sorted([sum(x) for x in values])

# most calories on 1 elf
print("part one:", elves[-1])

# sum of calories of the top 3 elves
print("part two:", sum(elves[-3:]))
