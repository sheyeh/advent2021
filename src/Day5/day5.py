import re
import numpy


def parse(value):
    return [int(i) for i in re.split(",| -> ", value)]


def my_range(i, j):
    return range(i, j + 1) if i < j else range(j, i + 1)


def increment(d, k):
    val = d.get(k)
    d[k] = val + 1 if val else 1


# diagram is represented as a dictionary where the key is an (x,y) coordinate
# and the value is the number of vents that go through (x,y)
diagram1 = {}  # represents horizontal and vertical vents
diagram2 = {}  # represents horizontal, vertical and diagonal vents
with open('day5.txt', 'r') as f:
    for line in f:
        x1, y1, x2, y2 = parse(line)
        if x1 == x2:  # horizontal
            for y in my_range(y1, y2):
                key = (x1, y)
                increment(diagram1, key)
                increment(diagram2, key)
        else:  # vertical and diagonal
            x = x1
            y = y1
            while x != x2 + numpy.sign(x2 - x1):
                key = (x, y)
                if y1 == y2:  # diagram1 is incremented only for vertical vents
                    increment(diagram1, key)
                increment(diagram2, key)
                x += numpy.sign(x2 - x1)
                y += numpy.sign(y2 - y1)

print("Part 1:", sum(map(lambda v: v > 1, diagram1.values())))
print("Part 2:", sum(map(lambda v: v > 1, diagram2.values())))
