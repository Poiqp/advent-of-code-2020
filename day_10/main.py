with open('input', 'r') as f:
    data_string = f.read().splitlines()
    data = [int(x) for x in data_string]


def part_one():

    data.append(max(data)+3)
    data.append(0)
    data.sort()
    jolt_1_diff = 0
    jolt_3_diff = 0

    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        if diff == 1:
            jolt_1_diff += 1
        elif diff == 3:
            jolt_3_diff += 1
    print(jolt_1_diff, jolt_3_diff)
    print(jolt_1_diff*jolt_3_diff)


def part_two():
    pass


part_one()
# part_two()
