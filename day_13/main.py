with open('input', 'r') as f:
    data_string = f.read().splitlines()
data = []
for line in data_string[1].split(','):
    if line != 'x':
        data.append(int(line))


def part_one():
    time = int(data_string[0])
    earliest_bus_line = [None, None]  # bus line , earliest bus time

    for bus in data:
        closest_bus = (time//bus)*bus + bus

        if earliest_bus_line[1] is None:
            earliest_bus_line[1] = closest_bus
            earliest_bus_line[0] = bus
            continue

        if closest_bus < earliest_bus_line[1]:
            earliest_bus_line[1] = closest_bus
            earliest_bus_line[0] = bus

    print((earliest_bus_line[1] - time)*earliest_bus_line[0])


def part_two():
    #
    pass


# part_one()
part_two()
