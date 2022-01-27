def parse(measurement):
    ret = []
    for char in measurement.rstrip():
        ret.append(int(char))
    return ret


hist = []
num_rows = 0
with open('day3.txt', 'r') as f:
    for line in f:
        num_rows += 1
        digits = parse(line)
        if hist:  # hist already populated, so not the first line
            for i in range(0, len(digits) - 1):
                hist[i] += digits[i]
        else:  # first line
            hist = digits

gamma = 0
for count in hist:
    gamma *= 2
    gamma += 1 if count > num_rows / 2 else 0

epsilon = 2 ** len(hist) - 1 - gamma

print("Part 1:", gamma * epsilon)
