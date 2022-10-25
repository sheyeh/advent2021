import numpy
import re

with open('day17.txt', 'r') as f:
    for line in f:
        numbers = re.findall(r'-?\d+', line)
x_left, x_right, y_bottom, y_top = [int(n) for n in numbers]


def trajectory(x_speed, y_speed, x_0, x_1, y_0, y_1):
    x = 0
    y = 0
    x_s = x_speed
    y_s = y_speed
    inside = False
    path = [[0, 0]]
    while y > y_0 and x < x_1:
        x = x + x_s
        y = y + y_s
        x_s = x_s - numpy.sign(x_s)
        y_s = y_s - 1
        if x_0 <= x <= x_1 and y_0 <= y <= y_1:
            inside = True
        path.append([x, y])
    return path if inside else None


x_min_speed = int(numpy.sqrt((1 + 4 * 96)) / 2 + 1)
peak = 0
for x_sp in range(x_min_speed, x_right + 1):
    for y_sp in range(-y_bottom + 1):
        tr = trajectory(x_sp, y_sp, x_left, x_right, y_bottom, y_top)
        if tr:
            y_max = max([s[1] for s in tr])
            peak = max(y_max, peak)

print(peak)
