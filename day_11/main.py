import copy

with open('input', 'r') as f:
    data_string = f.read().splitlines()
    data = [[char for char in word] for word in data_string]


def count_adjacent_occupied(y, x, data):
    adjacent = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    occupied = 0
    for position in adjacent:
        adj_x = x+position[0]
        adj_y = y+position[1]
        if (0 <= adj_x <= len(data[0])-1) and (0 <= adj_y <= len(data)-1):
            if data[y+position[1]][x+position[0]] == '#':
                occupied += 1
    return occupied


def part_one(data):

    next_round = copy.deepcopy(data)

    while True:
        for y, row in enumerate(data):
            for x, seat in enumerate(row):
                if seat == 'L':
                    if not count_adjacent_occupied(y, x, data):
                        next_round[y][x] = '#'
                    else:
                        next_round[y][x] = 'L'
                elif seat == '#':
                    if count_adjacent_occupied(y, x, data) >= 4:
                        next_round[y][x] = 'L'
                    else:
                        next_round[y][x] = '#'
        # print('Curr round: ')
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in data]), '\n')
        # print('Next round: ')
        # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in next_round]), '\n')

        if data == next_round:
            print('Seats occupied: ', sum(x.count('#') for x in next_round))
            break
        else:
            data, next_round = next_round, data


def part_two(data):
    pass


# part_one(data)
# part_two(data)
