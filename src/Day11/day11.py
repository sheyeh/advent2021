levels = []
with open('day11.txt', 'r') as f:
    for line in f:
        levels.append([int(i) for i in line.rstrip()])

N: int = len(levels)


def increment():
    for i in range(N):
        for j in range(N):
            levels[i][j] += 1


def plus_minus_one(k):
    return range(max(0, k - 1), min(N, k + 2))


def flash():
    still_flashing = True
    while still_flashing:
        still_flashing = False
        for i in range(N):
            for j in range(N):
                if levels[i][j] > 9:
                    still_flashing = True
                    levels[i][j] = -1000
                    for _i in plus_minus_one(i):
                        for _j in plus_minus_one(j):
                            if _i == i and _j == j:
                                continue
                            levels[_i][_j] += 1

    num_flashes = 0
    for i in range(N):
        for j in range(N):
            if levels[i][j] < 0:
                levels[i][j] = 0
                num_flashes += 1

    return num_flashes


total_flashes = 0
for i in range(100):
    increment()
    total_flashes += flash()

print("Part 1:", total_flashes)

f = 0
while f < N * N:
    increment()
    f = flash()
    i += 1

print("Part 2:", i + 1)
