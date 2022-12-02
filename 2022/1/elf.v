import arrays
import os

filename := os.args[1]
println(filename)

data := os.read_file(filename)?
groups := data.split("\n\n")

mut elves := []int{}
for group in groups {
	elves << arrays.sum(group.split("\n").map(it.int()))?
}
elves.sort()

// most calories on 1 elf
println("part one: ${elves.last()}")

// sum of calories of the top 3 elves
println("part two: ${arrays.sum(elves#[-3..])}")
