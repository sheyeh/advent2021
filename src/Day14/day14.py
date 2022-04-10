import collections

polymer = None
rules = {}

with open('day14.txt', 'r') as f:
    for line in f:
        if not polymer:
            polymer = line.rstrip()
        if ">" in line:
            split = line.rstrip().split(" -> ")
            rules[split[0]] = split[1]

for x in range(10):
    new_polymer = []
    for pos in range(len(polymer) - 1):
        pair = polymer[pos:pos + 2]
        new_polymer.append(polymer[pos])
        if rules.get(pair):
            new_polymer.append((rules.get(pair)))
    new_polymer.append(polymer[-1])
    polymer = "".join(new_polymer)

hist = collections.Counter(new_polymer)
print("Part 1:", max(hist.values()) - min(hist.values()))
