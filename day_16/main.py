import re

with open('input', 'r') as f:
    data_string = f.read().splitlines()


# ranges
ranges = []
for line in data_string:
    if line == '':
        break
    m = re.search(r'(\d+)-(\d+)\sor\s(\d+)-(\d+)', line)
    ranges.append([int(m[1]), int(m[2])])
    ranges.append([int(m[3]), int(m[4])])

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
    pass


part_one()