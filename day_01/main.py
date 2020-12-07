with open('input', 'r') as f:
    data_string = f.read().splitlines()
    data = [int(x) for x in data_string]

data_set = set(data)
data.sort(reverse=True)


def part_one():
    for number in data:
        rest = 2020 - number
        if rest in data_set:
            print(number, rest, rest*number)
            return


def part_two():
    for i, number in enumerate(data):
        rest1 = 2020 - number
        for number2 in data[i:]:
            if number2 < rest1:
                rest2 = rest1 - number2
                if rest2 in data_set:
                    print(number, number2, rest2, number*number2*rest2)
                    return
