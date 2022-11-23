import itertools
import re


class Cuboid:
    def __init__(self, state, x0, x1, y0, y1, z0, z1):
        self.on_off = state
        self.x_from = x0
        self.x_to = x1
        self.y_from = y0
        self.y_to = y1
        self.z_from = z0
        self.z_to = z1

    def covers(self, x_coord, y_coord, z_coord):
        return self.x_from <= x_coord <= self.x_to \
               and self.y_from <= y_coord <= self.y_to \
               and self.z_from <= z_coord <= self.z_to

    def overlaps(self, other):
        return self.x_from <= other.x_from and self.x_to >= other.x_to \
               and self.y_from <= other.y_from and self.y_to >= other.y_to \
               and self.z_from <= other.z_from and self.z_to >= other.z_to

    def partial_cover_x(self, other):
        return (self.x_from <= other.x_from <= self.x_to or self.x_from <= other.x_to <= self.x_to) \
               and self.y_from <= other.y_from and self.y_to >= other.y_to \
               and self.z_from <= other.z_from and self.z_to >= other.z_to

    def partial_cover_y(self, other):
        return self.x_from <= other.x_from and self.x_to >= other.x_to \
               and (self.y_from <= other.y_from <= self.y_to or self.y_from <= other.y_to <= self.y_to) \
               and self.z_from <= other.z_from and self.z_to >= other.z_to

    def partial_cover_z(self, other):
        return self.x_from <= other.x_from and self.x_to >= other.x_to \
               and self.y_from <= other.y_from and self.y_to >= other.y_to \
               and (self.z_from <= other.z_from <= self.z_to or self.z_from <= other.z_to <= self.z_to)

    def __str__(self):
        return "{} : {}..{}, {}..{}, {}..{}".format(
            "on" if self.on_off else "off",
            self.x_from, self.x_to, self.y_from, self.y_to, self.z_from, self.z_to)


cuboids = []
x_values = []
y_values = []
z_values = []
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


# If a cuboid overlaps a lower numbered cuboid than the lower numbered one can be ignored
def remove_overlaps(overlapping_cuboids):
    non_overlapping_cuboids = []
    for c1 in range(len(overlapping_cuboids)):
        cub1 = overlapping_cuboids[c1]
        overlap = any([overlapping_cuboids[c2].overlaps(cub1) for c2 in range(c1 + 1, len(overlapping_cuboids))])
        if not overlap:
            non_overlapping_cuboids.append(cub1)
    return non_overlapping_cuboids


def modify_partial_cover(partially_cover_cuboids):
    for c1 in range(len(partially_cover_cuboids)):
        cub1 = partially_cover_cuboids[c1]
        for c2 in range(c1 + 1, len(partially_cover_cuboids)):
            cub2 = partially_cover_cuboids[c2]
            if cub2.partial_cover_x(cub1):
                if cub2.x_from <= cub1.x_from <= cub2.x_to:
                    cub1.x_from = cub2.x_to
                else:
                    cub1.x_to = cub2.x_from
            elif cub2.partial_cover_y(cub1):
                if cub2.y_from <= cub1.y_from <= cub2.y_to:
                    cub1.y_from = cub2.y_to
                else:
                    cub1.y_to = cub2.y_from
            elif cub2.partial_cover_z(cub1):
                if cub2.z_from <= cub1.z_from <= cub2.z_to:
                    cub1.z_from = cub2.z_to
                else:
                    cub1.z_to = cub2.z_from


cuboids = remove_overlaps(cuboids)
modify_partial_cover(cuboids)

count = 0
for cuboid in cuboids:
    x_values.append(cuboid.x_from)
    x_values.append(cuboid.x_to)
    x_values.append(cuboid.x_to + 1)
    y_values.append(cuboid.y_from)
    y_values.append(cuboid.y_to)
    y_values.append(cuboid.y_to + 1)
    z_values.append(cuboid.z_from)
    z_values.append(cuboid.z_to)
    z_values.append(cuboid.z_to + 1)


def list_set_sorted(values, limit_to_fifty=True):
    if limit_to_fifty:
        min_coordinate = -50
        max_coordinate = 50
    else:
        min_coordinate = min(values)
        max_coordinate = max(values)

    values.append(max_coordinate + 1)
    return sorted(list(set([v for v in values if min_coordinate <= v <= max_coordinate + 1])))


x_values = list_set_sorted(x_values, False)
y_values = list_set_sorted(y_values, False)
z_values = list_set_sorted(z_values, False)

total_steps = len(x_values) * len(y_values) * len(z_values)
print(total_steps)

steps = 0
for x, y, z in itertools.product(range(len(x_values) - 1), range(len(y_values) - 1), range(len(z_values) - 1)):
    steps += 1
    if steps % 500000 == 0:
        print("{} ({}%)".format(steps, int(10000 * steps / total_steps * 100) / 10000))
    num_cubes = (x_values[x + 1] - x_values[x]) \
                * (y_values[y + 1] - y_values[y]) \
                * (z_values[z + 1] - z_values[z])
    # print(x_values[x],y_values[y],z_values[z], num_cubes)
    for cuboid in reversed(cuboids):
        if cuboid.covers(x_values[x], y_values[y], z_values[z]):
            if cuboid.on_off:
                # print("         ",cuboid, num_cubes, "*" if num_cubes > 1 else "")
                count += num_cubes
            break

print("Part 1:", count)
