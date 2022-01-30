from scipy.optimize import minimize_scalar


with open('day7.txt', 'r') as f:
    for line in f:
        hor = [int(i) for i in line.split(",")]


def cost(center):
    return sum(abs(h - center) for h in hor)


def crab_cost(dist):
    abs_dist = abs(dist)
    return int(abs_dist * (abs_dist + 1) / 2)


def cost2(center):
    return sum(crab_cost(h - center) for h in hor)


def min_cost(func):
    low = min(hor)
    high = max(hor)
    while True:
        # Evaluate at mid point and +/- 1
        mid = int((low + high) / 2)
        mid_val_m1 = func(mid - 1)
        mid_val = func(mid)
        mid_val_p1 = func(mid + 1)
        # if mid point value is lower than both then minimum found
        if mid_val < mid_val_m1 and mid_val < mid_val_p1:
            break
        # If mid value is lower than the mid -1 then move right
        if mid_val < mid_val_m1:
            low = mid
        # Otherwise move left
        else:
            high = mid

    return mid_val


# >>>>> Part 1 <<<<<
# Using SciPy
res = minimize_scalar(cost, bounds=(min(hor), max(hor)), method='bounded')
# res.x can be non-integer, so check the integers below and above, and pick the minimum
print("Part 1:", min(cost(int(res.x)), cost(int(res.x) + 1)))

# Alternative
print("Part 1 (alt):", min_cost(cost))

# >>>>> Part 2 <<<<<
# Using SciPy
res2 = minimize_scalar(cost2, bounds=(min(hor), max(hor)), method='bounded')
print("Part 2:", min(cost2(int(res2.x)), cost2(int(res2.x) + 1)))

# Alternative
print("Part 2 (alt):", min_cost(cost2))
