from src.Day13.Dot import Dot

folding_instructions = []
input_dots = []

with open('day13.txt', 'r') as f:
    for line in f:
        if "," in line:
            input_dots.append(Dot(line))
        if line.startswith("fold"):
            folding_instructions.append((line[11:12], int(line[13:].rstrip())))

new_dots = {dot.fold(folding_instructions[0]) for dot in input_dots}

print("Part 1:", len(new_dots))

dots = input_dots
for instruction in folding_instructions:
    new_dots = {dot.fold(instruction) for dot in input_dots}
    dots = new_dots

width = max(dot.x for dot in dots) + 1
height = max(dot.y for dot in dots) + 1
line = " " * width
lines = []
for i in range(height):
    lines.append(list(line))

for dot in dots:
    lines[dot.y][dot.x] = "#"

print("Part 2:")
for line in lines:
    print("".join(line))
