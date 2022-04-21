'''
In this version we keep track of character and pair
counts instead of constructing the full string.
'''

polymer = None
rules = {}

with open('day14.txt', 'r') as f:
    for line in f:
        if not polymer:
            polymer = line.rstrip()
        if ">" in line:
            split = line.rstrip().split(" -> ")
            rules[split[0]] = split[1]

pairs = {}
hist = {}

for c in polymer:
    if hist.get(c):
        hist[c] += 1
    else:
        hist[c] = 1

for i in range(len(polymer) -1):
    pair = polymer[i:i+2]
    if pairs.get(pair):
        pairs[pair] += 1
    else:
        pairs[pair] = 1

for i in range(40):
    keys = list(pairs.keys())
    new_pairs = {}
    for pair in keys:
        c = rules.get(pair)
        if hist.get(c):
            hist[c] += pairs.get(pair)
        else:
            hist[c] = pairs.get(pair)
        new_pair_1 = pair[0] + c
        if new_pairs.get(new_pair_1):
            new_pairs[new_pair_1] += pairs.get(pair)
        else:
            new_pairs[new_pair_1] = pairs.get(pair)
        new_pair_2 = c + pair[1]
        if new_pairs.get(new_pair_2):
            new_pairs[new_pair_2] += pairs.get(pair)
        else:
            new_pairs[new_pair_2] = pairs.get(pair)
    pairs = dict(new_pairs)

print("Part 2:", max(hist.values()) - min(hist.values()))