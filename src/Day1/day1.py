###

def count(list, window):
    c = 0
    for i in range(len(list) - window + 2):
        if sum(list[i + 1 : i + window + 1]) > sum(list[i : i + window]):
            c += 1
    return c

my_list = []
with open('day1.txt', 'r') as f:
    for line in f:
        my_list.append(int(line))

print("Part 1 :", count(my_list, 1))
print("Part 2 :", count(my_list, 3))
