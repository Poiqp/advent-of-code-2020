with open('input', 'r') as f:
    data_string = f.read().splitlines()
    data = [x.replace('-', ' ').replace(':', '').split(' ') for x in data_string]


def part_one():
    counter = 0
    for entry in data:
        if int(entry[0]) <= entry[3].count(entry[2]) <= int(entry[1]):
            counter += 1
    print(counter)


def part_two():
    counter = 0
    for entry in data:
        if (entry[3][int(entry[0])-1] == entry[2]) is not (entry[3][int(entry[1])-1] == entry[2]):
            counter += 1
    print(counter)
