with open('input', 'r') as f:
    data_string = f.read().splitlines()
    data = [list(x) for x in data_string]


def part_one():
    trees_counter = 0
    width = len(data[0])
    x = 0

    for row in range(1, len(data)):
        x = (x + 3) % width
        if data[row][x] == '#':
            trees_counter += 1

    print(trees_counter)


def part_two():
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    trees_counter = []
    width = len(data[0])
    height = len(data)

    for slope in slopes:
        x = 0
        y = 0
        end_of_slope = False
        counter = 0

        while not end_of_slope:
            x = (x + slope[0]) % width
            y += slope[1]
            if y < height:
                if data[y][x] == '#':
                    counter += 1
            else:
                end_of_slope = True
        trees_counter.append(counter)

    multiplication = 1
    for count in trees_counter:
        multiplication *= count
    print(trees_counter, multiplication)
