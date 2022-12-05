{:ok, data} = File.read(System.argv())

elves =
  Enum.sort(
    for x <- String.split(data, "\n\n"),
        do:
          String.split(x, "\n", trim: true)
          |> Enum.map(&String.to_integer/1)
          |> Enum.sum()
  )

# most calories on 1 elf
IO.puts("part one: #{List.last(elves)}")

# sum of calories of the top 3 elves
IO.puts("part two: #{Enum.sum(Enum.take(elves, -3))}")
