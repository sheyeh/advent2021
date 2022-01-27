def parse(measurement):
    ret = []
    for char in measurement.rstrip():
        ret.append(int(char))
    return ret


def rating(all_samples, is_ox):
    i = 0
    while len(all_samples) > 1:
        split_samples = {0: [], 1: []}
        for sample in all_samples:
            split_samples.get(sample[i]).append(sample)
        zero_samples = split_samples.get(0)
        one_samples = split_samples.get(1)
        if is_ox:
            all_samples = zero_samples if len(zero_samples) > len(one_samples) else one_samples
        else:
            all_samples = zero_samples if len(zero_samples) <= len(one_samples) else one_samples
        i += 1

    return all_samples[0]


def decimal(binary):
    dec = 0
    for bit in binary:
        dec *= 2
        dec += bit
    return dec


samples = []
with open('day3.txt', 'r') as f:
    for line in f:
        samples.append(parse(line))

oxygen_generator_rating = rating(samples, True)
co2_scrubber_rating = rating(samples, False)

print("Part 2:", decimal(oxygen_generator_rating) * decimal(co2_scrubber_rating))
