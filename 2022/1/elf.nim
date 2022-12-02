import algorithm, math, os, sequtils, strformat, strutils, sugar

let 
    data = read_file(param_str(1))
    groups = data.split("\n\n")
    values = groups.map(x => x.split("\n").filter(x => x.len > 0).map(x => parse_int(x))).map(x => x.sum())
    elves = values.sorted()

# most calories on 1 elf
echo fmt"part one: {elves[^1]}"

# sum of calories of the top 3 elves
echo fmt"part two: {elves[^3..^1].sum()}"
