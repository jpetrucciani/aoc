import sys

data = [x for x in open(sys.argv[1], "r").read().split("\n") if x]
points = [3, 0, 6]
points_2 = [0, 3, 6]


def parse(game: str):
    return ((ord(x) % 23) - 18 for x in game.upper().split(" "))


def rps_1(game: str) -> int:
    e, p = parse(game)
    meme = (e - p + 3) % 3
    return points[meme] + p


def rps_2(game: str) -> int:
    e, wl = parse(game)
    meme = (e + ((wl + 1) % 3)) % 3
    return (meme if meme else 3) + points_2[wl - 1]


# strategy guide, enemy -> player
rounds_1 = [rps_1(x) for x in data]
print(f"part 1: {sum(rounds_1)}")

# strategy guide, enemy -> result
rounds_2 = [rps_2(x) for x in data]
print(f"part 2: {sum(rounds_2)}")
