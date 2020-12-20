import re

with open('test_input', 'r') as f:
    data_string = f.read().splitlines()


# ranges
ranges = []
for line in data_string:
    if line == '':
        break
    m = re.search(r'(\d+)-(\d+)\sor\s(\d+)-(\d+)', line)
    ranges.append([int(m[1]), int(m[2])])
    ranges.append([int(m[3]), int(m[4])])

# fields
fields = []
for line in data_string:
    if line == '':
        break
    m = re.search(r'(\d+)-(\d+)\sor\s(\d+)-(\d+)', line)
    fields.append([int(m[1]), int(m[2]), int(m[3]), int(m[4])])

# my ticket
my_ticket = (data_string[data_string.index('your ticket:') + 1]).split(',')
my_ticket = [int(x) for x in my_ticket]

# nearby tickets
nearby_tickets = []
idx = data_string.index('nearby tickets:') + 1
for i in range(idx, len(data_string)):
    ticket_numbers = [int(x) for x in data_string[i].split(',')]
    nearby_tickets.append(ticket_numbers)


def part_one():
    domain_set = set()
    for domain in ranges:
        for i in range(domain[0], domain[1]+1):
            domain_set.add(i)

    ticket_scanning_error_rate = 0
    for ticket in nearby_tickets:
        for number in ticket:
            if number not in domain_set:
                ticket_scanning_error_rate += number
    print(ticket_scanning_error_rate)


def part_two():
    domain_set = set()
    for domain in ranges:
        for i in range(domain[0], domain[1]+1):
            domain_set.add(i)

    for ticket in nearby_tickets:
        for number in ticket:
            if number not in domain_set:
                nearby_tickets.remove(ticket)

    possibilities = []
    for i in range(0, len(nearby_tickets[0])):
        possibilities.append([x for x in range(0, len(nearby_tickets[0]))])

    # columns
    for i in range(0, len(nearby_tickets[0])):
        # numbers in tickets
        for ticket in nearby_tickets:
            for idx, field in enumerate(fields):
                if not (field[0] <= ticket[i] <= field[1]) or (field[2] <= ticket[i] <= field[1]):
                    print(possibilities[i], idx)
                    possibilities[i].remove(idx)
    print(possibilities)


part_one()
part_two()
