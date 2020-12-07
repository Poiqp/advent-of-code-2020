import re
with open('input', 'r') as f:
    data_string = f.read().splitlines()

# im really sick of this, not gonna bother with optimizing it or basically doing anything with it
# its really bad part one is mediocre at best
# but part two is abismal
# Ive got work tmr need to go sleep
# but Ive made myself a promise to do this everyday and finish everyday
# so thats it, works but dont look into the code

# forget that it doesnt even work
# works on examples given on site but not on real input


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def part_one():
    data = []
    graph = {}

    for line in data_string:
        bag_color = re.match(r"^(\S+\s+\S+)", line)
        contents = re.findall(r"(\d\s\S+\s\S+)", line)

        if contents:
            contents_bags = [' '.join(x.split(' ')[1:3]) for x in contents]
        else:
            contents_bags = 'end'

        if bag_color[0] not in graph:
            graph[bag_color[0]] = contents_bags

    paths = set()
    for node in graph:
        path = find_path(graph, node, 'shiny gold')
        if path != None and len(path) != 1:
            for node in path:
                paths.add(node)
    print(len(paths) - 1)


def find_valued_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start[0] not in graph:
        return []
    paths = []
    for node in graph[start[0]]:
        if node not in path:
            newpaths = find_valued_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def part_two():
    data = []
    graph = {}

    for line in data_string:
        bag_color = re.match(r"^(\S+\s+\S+)", line)
        contents = re.findall(r"(\d\s\S+\s\S+)", line)

        if contents:
            contents_bags = [(' '.join(x.split(' ')[1:3]), int(x.split(' ')[0])) for x in contents]
        else:
            contents_bags = [('end', 1)]

        if bag_color[0] not in graph:
            graph[bag_color[0]] = contents_bags

    paths = find_valued_path(graph, ('shiny gold', 1), ('end', 1))

    total_bags = 0
    unique_starts = {}
    for path in paths:
        path.pop(0)
        path.pop(-1)

        # occurances | power
        if path[0][0] in unique_starts:
            unique_starts[path[0][0]][0] += 1
        else:
            unique_starts[path[0][0]] = [1, path[0][1]]
        print(path)

        sum = 0
        for i, node in enumerate(path):

            tmp = 1
            if i == 0:
                tmp = node[1]
            else:
                for j in range(-1, i):
                    tmp *= path[j][1]
            print(tmp)
            sum += tmp

        total_bags += sum

    # lacks if exactly one is present
    print(unique_starts)
    for element in unique_starts:
        if unique_starts[element][0] != 1:
            total_bags -= unique_starts[element][1]

    print('total bags', total_bags)


part_two()
