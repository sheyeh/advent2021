import numpy as np
from Match import Match

I0 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])   # no rotation
Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])  # rotation around x
Ry = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])  # rotation around y
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])  # rotation around z

# Generate the 24 possible rotations
# See https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
rotations = []
S = I0
for r in range(6):
    S = Rx @ S
    rotations.append(S)
    for t in range(4):
        S = S if t == 0 else Rz @ S if r % 2 else Rz @ Rz @ Rz @ S
        desc = "{} rolls and {} turns".format(r, t)
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

def diff(l1, l2):
    for rotation in rotations:
        d = {}
        d1 = {}
        d2 = {}
        for v1 in l1:
            for v2 in l2:
                result = v1 - rotation @ v2
                result_key = str(result)
                d.setdefault(result_key, 0)
                d1.setdefault(result_key, [])
                d2.setdefault(result_key, [])
                d[result_key] += 1
                d1[result_key].append(v1)
                d2[result_key].append(v2)
                if d[result_key] == 12:
                    return True, result, rotation
    return None, None, None

matches = {}
for i1 in range(len(beacons)):
    beacons1 = beacons[i1]
    for i2 in range(i1 + 1, len(beacons)):
        beacons2 = beacons[i2]
        found, delta, rotation = diff(beacons1, beacons2)
        if found:
            print(i1, i2, delta, rotation)
            matches.setdefault(i2, {})
            matches[i2][i1] = str(rotation)
