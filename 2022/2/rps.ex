{:ok, data} = File.read(System.argv())

lines = String.split(data, "\n", trim: true)

defmodule Util do
  def dict(list) do
    list |> Enum.with_index() |> Enum.map(fn {v, k} -> {k, v} end) |> Map.new()
  end

  def mod3(val) do
    Kernel.rem(val, 3)
  end
end

defmodule RPS do
  @points Util.dict([3, 0, 6])
  @points_2 Util.dict([0, 3, 6])

  def parse(game) do
    for x <- String.split(game, " ", trim: true, parts: 2),
        do:
          x
          |> :binary.first()
          |> Integer.mod(23)
          |> Kernel.-(18)
  end

  def game_1(game) do
    [e, p] = parse(game)
    @points[Util.mod3(e - p + 3)] + p
  end

  def game_2(game) do
    [e, wl] = parse(game)
    meme = Util.mod3(e + Util.mod3(wl + 1))
    if(meme == 0, do: 3, else: meme) + @points_2[wl + -1]
  end
end

# strategy guide, enemy -> player
rounds_1 = for x <- lines, do: RPS.game_1(x)
IO.puts("part one: #{Enum.sum(rounds_1)}")

# strategy guide, enemy -> result
rounds_2 = for x <- lines, do: RPS.game_2(x)
IO.puts("part two: #{Enum.sum(rounds_2)}")
