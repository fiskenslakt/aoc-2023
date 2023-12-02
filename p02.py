import re

from aocd import data, submit

# import pudb;pu.db

# data = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

blue_p = re.compile(r'(\d+)\sblue')
red_p = re.compile(r'(\d+)\sred')
green_p = re.compile(r'(\d+)\sgreen')

valid_games = []

for game in data.splitlines():
    valid = True
    gid, cubes = game.split(': ')
    gid = gid.split()[1]
    # if gid == '3':
    #     import pudb;pu.db

    sets = cubes.split('; ')
    for s in sets:
        if match := blue_p.search(s):
            b_cubes = int(match[1])
        else:
            b_cubes = 0

        if match := red_p.search(s):
            r_cubes = int(match[1])
        else:
            r_cubes = 0

        if match := green_p.search(s):
            g_cubes = int(match[1])
        else:
            g_cubes = 0

        if b_cubes > MAX_BLUE or r_cubes > MAX_RED or g_cubes > MAX_GREEN:
            valid = False
            break

    if not valid:
        continue

    valid_games.append(int(gid))

# print(valid_games)
# print(sum(valid_games))
submit(sum(valid_games))
