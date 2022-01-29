import re


def parse(value):
    return [int(i) for i in re.split(",| -> ", value)]


def my_range(i, j):
    return range(i, j + 1) if i < j else range(j, i + 1)


# diagram is represented as a dictionary where the key is an x-y coordinate
# and the value is the number of vents that go through x-y
diagram = {}
with open('day5.txt', 'r') as f:
    for line in f:
        x1, y1, x2, y2 = parse(line)
        if x1 == x2:
            for y in my_range(y1, y2):
                key = (x1, y)
                val = diagram.get(key)
                diagram[key] = val + 1 if val else 1
        if y1 == y2:
            for x in my_range(x1, x2):
                key = (x, y1)
                val = diagram.get(key)
                diagram[key] = val + 1 if val else 1

print("Part 1:", sum(map(lambda v: v > 1, diagram.values())))
