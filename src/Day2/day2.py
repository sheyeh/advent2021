def parse(line):
    direction, value = line.split(" ")
    val = int(value)
    return {
        'up' : [0, -val],
        'down': [0, val],
        'forward': [val, 0]
    }[direction]

horizontal = 0
depth = 0

with open('day2.txt', 'r') as f:
    for line in f:
        x, y = parse(line)
        horizontal += x
        depth += y

print("Part 1:", horizontal * depth)

aim = 0
horizontal = 0
depth = 0

with open('day2.txt', 'r') as f:
    for line in f:
        direction, value = line.split(" ")
        val = int(value)
        if direction == 'up':
            aim -= val
        if direction == 'down':
            aim += val
        if direction == 'forward':
            horizontal += val
            depth += aim * val

print("Part 2:", horizontal * depth)