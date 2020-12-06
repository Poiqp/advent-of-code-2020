import math

with open('input', 'r') as f:
    data = f.read().splitlines()


def part_one():
    seatIDs = set()
    for word in data:
        upper = 127
        lower = 0
        col_lower = 0
        col_upper = 7
        for letter in range(0, 7):
            if word[letter] == 'F':
                upper = math.floor(upper - ((upper-lower)/2))
            elif word[letter] == 'B':
                lower = math.ceil(lower + ((upper-lower)/2))
        for letter in range(7, 10):
            if word[letter] == 'L':
                col_upper = math.floor(col_upper - ((col_upper-col_lower)/2))
            elif word[letter] == 'R':
                col_lower = math.ceil(col_lower + ((col_upper-col_lower)/2))
        seatIDs.add(lower*8 + col_lower)
    print(max(seatIDs))


def part_two():
    seatIDs = []
    for word in data:
        upper = 127
        lower = 0
        col_lower = 0
        col_upper = 7
        for letter in range(0, 7):
            if word[letter] == 'F':
                upper = math.floor(upper - ((upper-lower)/2))
            elif word[letter] == 'B':
                lower = math.ceil(lower + ((upper-lower)/2))
        for letter in range(7, 10):
            if word[letter] == 'L':
                col_upper = math.floor(col_upper - ((col_upper-col_lower)/2))
            elif word[letter] == 'R':
                col_lower = math.ceil(col_lower + ((col_upper-col_lower)/2))
        seatIDs.append(lower*8 + col_lower)
    seatIDs.sort()
    missing_seat = [x for x in range(seatIDs[0], seatIDs[-1]+1) if x not in seatIDs]
    print(missing_seat)
