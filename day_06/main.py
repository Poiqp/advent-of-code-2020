with open('input', 'r') as f:
    data_string = f.read().splitlines()

# make sure that your input ends with a blank line


def part_one():
    data = []
    tmp = set()
    for line in data_string:
        if line != '':
            for letter in line:
                tmp.add(letter)
        else:
            data.append(tmp)
            tmp = set()

    sum = 0
    for answer in data:
        print(len(answer))
        sum += len(answer)
    print(sum)


def part_two():
    data = []
    tmp = []
    for line in data_string:
        if line != '':
            tmp.append(line)
        else:
            data.append(tmp)
            tmp = []

    count = 0
    for group in data:
        set_list = []
        for person in group:
            set_list.append(set(person))
        intersection = set.intersection(*set_list)
        count += len(intersection)

    print(count)
