import re
from cuboid import Cuboid


cuboids = []
with open('day22.txt', 'r') as f:
    for line in f:
        tokens = re.split("[ xyz=.,]", line.rstrip())
        on_off = tokens[0] == "on"
        x_from = int(tokens[3])
        x_to = int(tokens[5])
        y_from = int(tokens[8])
        y_to = int(tokens[10])
        z_from = int(tokens[13])
        z_to = int(tokens[15])
        cuboids.append(Cuboid(on_off, x_from, x_to, y_from, y_to, z_from, z_to))


def count_on(the_cuboids, trimmer=None):
    free_cuboids = []
    for c1 in range(len(the_cuboids)):
        cub1 = the_cuboids[c1].trim(trimmer)
        if cub1 is None:
            continue
        list1 = [cub1]
        for c2 in range(c1 + 1, len(the_cuboids)):
            cub2 = the_cuboids[c2].trim(trimmer)
            if cub2 is None:
                continue
            list2 = []
            for cub in list1:
                list2 += cub2.dismantle(cub)
            list1 = list2
        free_cuboids.append(list1)

    return sum([sum([c.volume() if c.on_off else 0 for c in cc]) for cc in free_cuboids])


print(count_on(cuboids, Cuboid(True, -50, 50, -50, 50, -50, 50)))
print(count_on(cuboids))
