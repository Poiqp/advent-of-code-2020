with open('input', 'r') as f:
    data_string = f.read().splitlines()
    data = [int(x) for x in data_string]


def part_one():

    preambule_len = 25
    avail = [data[x] for x in range(0, preambule_len)]

    for number in range(preambule_len, len(data)):
        possible = []
        for elem in avail:
            if elem < data[number]:
                possible.append(elem)

        avail.pop(0)
        avail.append(data[number])

        perm = [(a, b) for idx, a in enumerate(possible) for b in possible[idx + 1:]]

        number_is_ok = False
        for i in list(perm):
            try:
                if i[0] + i[1] == data[number]:
                    number_is_ok = True
                    break
            except:
                break

        if number_is_ok == False:
            print(data[number])


def count_till_too_much(data, invalid_number):
    sum = 0
    tmp = []

    for i in data:
        if (sum == invalid_number) and (len(tmp) > 2):
            # recursion problem
            # return sum, tmp
            answer = str(min(tmp) + max(tmp))
            exit(answer)
        elif sum > invalid_number:
            data.pop(0)
            count_till_too_much(data, invalid_number)
        else:
            sum += i
            tmp.append(i)


def part_two():
    invalid_number = 31161678
    # invalid_number = 127

    print(count_till_too_much(data, invalid_number))


# part_one()
# part_two()
