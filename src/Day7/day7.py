from scipy.optimize import minimize_scalar


with open('day7.txt', 'r') as f:
    for line in f:
        hor = [int(i) for i in line.split(",")]


def cost(center):
    return sum(abs(h - center) for h in hor)


# Using SciPy
res = minimize_scalar(cost, bounds=(min(hor), max(hor)), method='bounded')
print("Part 1:", cost(round(res.x)))
