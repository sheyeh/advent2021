import numpy

fish = []
with open('day6.txt', 'r') as f:
    for line in f:
        fish = [int(i) for i in line.split(",")]


hist = list(numpy.histogram(fish, range(0, 10))[0])
for i in range(0, 80):
    h8 = hist[0]  # fish with zero days left
    hist = hist[1:]
    hist[6] += h8  # fish with zero days reset to 6, and get added to others that have 6 days left
    hist.append(h8)  # fish with zero days create new fish with 8 days

print("Part 1:", sum(hist))
