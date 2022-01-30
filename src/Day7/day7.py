from scipy.optimize import minimize_scalar


with open('day7.txt', 'r') as f:
    for line in f:
        hor = [int(i) for i in line.split(",")]


def cost(center):
    return sum(abs(h - center) for h in hor)


# Using SciPy
res = minimize_scalar(cost, bounds=(min(hor), max(hor)), method='bounded')
print("Part 1:", cost(round(res.x)))

# Alternative
low = min(hor)
high = max(hor)
while True:
    # Evaluate at mid point and +/- 1
    mid = int((low + high) / 2)
    mid_val_m1 = cost(mid - 1)
    mid_val = cost(mid)
    mid_val_p1 = cost(mid + 1)
    # if mid point value is lower than both then minimum found
    if mid_val < mid_val_m1 and mid_val < mid_val_p1:
        break
    # If mid value is lower than the mid -1 then move right
    if mid_val < mid_val_m1:
        low = mid
    # Otherwise move left
    else:
        high = mid

print("Part 1:", mid_val)
