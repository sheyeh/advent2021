from collections import Counter

total = 0
with open('day8.txt', 'r') as f:
    for line in f:
        signal_pattern, output_value = line.rstrip().split(" | ")
        values = output_value.split(" ")
        counter = Counter([len(i) for i in values])
        total += (counter[2] + counter[3] + counter[4] + counter[7])

print("Part 1:", total)
