import numpy as np

# Generate the 24 possible rotations
# See https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
I0 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])   # no rotation
Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])  # rotation around x
Ry = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])  # rotation around y - just for completeness, not used
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])  # rotation around z
rotations = []
S = I0
for r in range(6):
    S = Rx @ S
    rotations.append(S)
    for t in range(4):
        S = S if t == 0 else Rz @ S if r % 2 else Rz @ Rz @ Rz @ S
        rotations.append(S)


beacons = []
scanner_num = -1
with open('day19.txt', 'r') as f:
    for line in f:
        if line.startswith("--"):
            scanner_num += 1
            beacons.append([])
        elif line == "\n":
            pass
        else:
            beacons[scanner_num].append(np.array([int(s) for s in line.rstrip().split(",")]))

scanner_num += 1


def diff(l1, l2):
    for rotation in rotations:
        d = {}
        for v1 in l1:
            for v2 in l2:
                result = v1 - rotation @ v2
                result_key = str(result)
                d.setdefault(result_key, 0)
                d[result_key] += 1
                if d[result_key] == 12:
                    return True, result, rotation
    return None, None, None


matches = {}  # matches[i][j] has the transormation from scanner j to scanner i
for i1 in range(len(beacons)):
    beacons1 = beacons[i1]
    for i2 in range(i1 + 1, len(beacons)):
        beacons2 = beacons[i2]
        found, delta, rotation = diff(beacons1, beacons2)
        if found:
            matches.setdefault(i1, {})
            matches.setdefault(i2, {})
            inv_rot = np.linalg.inv(rotation)
            matches[i1][i2] = (rotation, delta)
            matches[i2][i1] = (inv_rot, -inv_rot @ delta)


# We can try to find shortest paths from each node to 0 but it could be simpler to just
# compute the transition matrices from each point to each point in maximum |scanners| steps
for n in range(scanner_num):
    matches2 = {}
    for i1 in range(scanner_num):
        matches2.setdefault(i1, {})
        for i2 in range(scanner_num):
            if i1 == i2:
                matches2[i1][i2] = (I0, [0,0,0])
            elif matches.get(i1) is not None and matches[i1].get(i2) is not None:
                matches2[i1][i2] = matches[i1][i2]
            else:
                for k in range(scanner_num):
                    if matches.get(k) is not None and matches[k].get(i2) is not None \
                        and matches.get(i1) is not None and matches[i1].get(k) is not None:
                            r2 = matches[i1][k][0] @ matches[k][i2][0]
                            d2 = matches[i1][k][0] @ matches[k][i2][1] + matches[i1][k][1]
                            matches2[i1][i2] = (r2, d2)
                            break
    matches = matches2

# for i1 in matches:
#     for i2 in matches[i1]:
#         print(">",i1,i2)


points = {}
for i in range(scanner_num):
    print("Scanner", i)
    m = matches[0][i]
    print(m)
    for b in beacons[i]:
        p = m[0] @ b + m[1]
        points[str(p).replace(".","")] = p
        print(b,"->",p)

print(points.keys())
print(len(points))

