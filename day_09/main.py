import re

with open('input', 'r') as f:
    data_string = f.read().splitlines()

data = []
for line in data_string:
    split = line.split(' ')
    command = split[0]
    value = eval(split[1])
    # command , value, repetition
    data.append([command, value, 0])


def run_commands(data, accumulator, pointer):
    command = data[pointer][0]

    if data[pointer][2] != 1:
        if command == 'acc':
            accumulator += data[pointer][1]
            data[pointer][2] += 1
            pointer += 1
            run_commands(data, accumulator, pointer)
        elif command == 'nop':
            data[pointer][2] += 1
            pointer += 1
            run_commands(data, accumulator, pointer)
        elif command == 'jmp':
            data[pointer][2] += 1
            pointer += data[pointer][1]
            run_commands(data, accumulator, pointer)
    else:
        return(print(accumulator))
    return None


def correct_the_boot(data, accumulator, pointer):
    command = data[pointer][0]

    if data[pointer][2] != 1:
        if command == 'acc':
            accumulator += data[pointer][1]
            data[pointer][2] += 1
            pointer += 1
            correct_the_boot(data, accumulator, pointer)
        elif command == 'nop':
            data[pointer][2] += 1
            pointer += 1
            correct_the_boot(data, accumulator, pointer)
        elif command == 'jmp':
            data[pointer][2] += 1
            pointer += data[pointer][1]
            correct_the_boot(data, accumulator, pointer)
    elif data[pointer][2] == 1:
        print('second to last')
        return 42
    else:
        return 42
    return 42


def part_one():
    accumulator = 0
    pointer = 0
    run_commands(data, accumulator, pointer)


def part_two():
    accumulator = 0
    pointer = 0
    print(correct_the_boot(data, accumulator, pointer))


part_two()
