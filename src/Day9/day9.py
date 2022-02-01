heights = []
with open('day9.txt', 'r') as f:
    for line in f:
        row = [int(i) for i in line.rstrip()]
        heights.append(row)

map_N = len(heights)
map_M = len(heights[0])


def height(x, y):
    return 10 if x < 0 or x >= map_N or y < 0 or y >= map_M else heights[x][y]


def risk(x, y):
    h = height(x, y)
    return h + 1 \
        if height(x - 1, y) > h and height(x + 1, y) > h and height(x, y - 1) > h and height(x, y + 1) > h \
        else 0


print("Part 1:", sum([risk(i, j) for i in range(0, map_N) for j in range(0, map_M)]))
