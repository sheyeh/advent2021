def parse(line):
    direction, value = line.split(" ")
    val = int(value)
    return {
        'up' : [0, -val],
        'down': [0, val],
        'forward': [val, 0]
    }[direction]

aim = 0 # in part 1 this is depth
horizontal = 0
depth_part_2 = 0 # only used in part 2

with open('day2.txt', 'r') as f:
    for line in f:
        x, y = parse(line)
        aim += y
        horizontal += x
        depth_part_2 += aim * x

print("Part 1:", horizontal * aim)
print("Part 2:", horizontal * depth_part_2)

