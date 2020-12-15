import re

with open('input', 'r') as f:
    data_string = f.read().splitlines()


def part_one():
    data = {}
    for line in data_string:
        if re.match(r'mask', line):
            mask = re.search(r'[0,1,X]+', line)[0]
        else:
            matcher = re.search(r'mem\[(\d+)\] = (\d+)', line)
            key = matcher[1]
            val = '{:036b}'.format(int(matcher[2]))
            result = ''
            for i in zip(mask, val):
                if i[0] == '0':
                    result += '0'
                elif i[0] == '1':
                    result += '1'
                elif i[0] == 'X':
                    result += i[1]
            data[key] = int(result, 2)
    print(sum(data.values()))


def part_two():
    pass


part_one()
