import re

with open('test_input', 'r') as f:
    data_string = f.read().splitlines()
    data = []
    for action in data_string:
        dir = re.match(r"\S", action)[0]
        value = int(re.search(r"\d+", action)[0])
        data.append([dir, value])


def part_one():
    sides = ['E', 'N', 'W', 'S']
    curr_dir = 0
    coords = [0, 0]      # [N,E]

    for action in data:
        dir = action[0]
        if dir == 'F':
            dir = sides[curr_dir]

        if dir == 'N':
            coords[0] += action[1]
        elif dir == 'S':
            coords[0] -= action[1]
        elif dir == 'E':
            coords[1] += action[1]
        elif dir == 'W':
            coords[1] -= action[1]
        elif dir == 'L':
            turn = int((action[1]/90) % 3)
            curr_dir += turn

            curr_dir = curr_dir % 4
        elif dir == 'R':
            turn = int((action[1]/90))
            curr_dir -= turn
            curr_dir = curr_dir % 4
        print('North:', coords[0], 'East:', coords[1], sides[curr_dir])

    print(abs(coords[0]) + abs(coords[1]))


def part_two():
    pass


part_one()
