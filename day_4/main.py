import re

# note: make sure that your imput ends with two blank lines

with open('input', 'r') as f:
    data_string = f.read().splitlines()

data = []
tmp = []
for line in data_string:
    if line != '':
        try:
            one_line_fields = line.split(' ')
            for field in one_line_fields:
                tmp.append(field)
        except:
            tmp.append(line)
    else:
        data.append(tmp)
        tmp = []

passports = []
tmp = {}
for passport in data:
    for field in passport:
        tmp[field.split(':')[0]] = field.split(':')[1]
    passports.append(tmp)
    tmp = {}


def part_one():
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid_passports = 0

    for passport in passports:
        if all(field in passport for field in required_fields):
            valid_passports += 1
    print(valid_passports)


def part_two():
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid_passports = 0

    for passport in passports:
        if all(field in passport for field in required_fields):
            if (1920 <= int(passport['byr']) <= 2002) and (2010 <= int(passport['iyr']) <= 2020) and (2020 <= int(passport['eyr']) <= 2030):
                height = re.split('(\d+)', passport['hgt'])
                if (height[2] == 'cm' and 150 <= int(height[1]) <= 193) or (height[2] == 'in' and 59 <= int(height[1]) <= 76):
                    if re.match(r"#[0-9a-f]{6}", passport['hcl']):
                        eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                        if (passport['ecl'] in eye_colours):
                            if re.match(r"[0-9]{9}", passport['pid']):
                                valid_passports += 1
    print(valid_passports)


part_one()
