import re

from aocd import data

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

valid_games = []
powers = []

for game in data.splitlines():
    valid = True
    game_id, cubes = game.split(': ')
    gid = game_id.split()[1]

    min_blue = 0
    min_red = 0
    min_green = 0

    sets = cubes.split('; ')
    for s in sets:
        b_cubes = 0
        r_cubes = 0
        g_cubes = 0

        if match := re.search(r'(\d+)\sblue', s):
            b_cubes = int(match[1])
        if match := re.search(r'(\d+)\sred', s):
            r_cubes = int(match[1])
        if match := re.search(r'(\d+)\sgreen', s):
            g_cubes = int(match[1])

        if b_cubes > MAX_BLUE or r_cubes > MAX_RED or g_cubes > MAX_GREEN:
            valid = False

        min_blue = max(min_blue, b_cubes)
        min_red = max(min_red, r_cubes)
        min_green = max(min_green, g_cubes)

    power = min_blue * min_red * min_green
    powers.append(power)

    if not valid:
        continue

    valid_games.append(int(gid))

print('Part 1:', sum(valid_games))
print('Part 2:', sum(powers))

