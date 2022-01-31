from collections import Counter


# Sort the characters of a string
def sorted_str(pattern):
    return ''.join(sorted(pattern))


# Checks if str2 contains any of the strings in str1
def contains_any(str1, str2):
    for s in str1:
        if s in str2:
            return True
    return False


# Checks if str2 contains all of the strings of str1
def contains_all(str1, str2):
    for s in str1:
        if s not in str2:
            return False
    return True


# Number of common characters in two strings
def overlap(str1, str2):
    overlap_count = 0
    for s in str1:
        overlap_count += 1 if s in str2 else 0
    return overlap_count


def decode(the_patterns):
    len_dict = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for pattern in the_patterns:
        len_dict[len(pattern)].append(pattern)
    return_value = {}
    # 1, 4, 7 and 8 have unique lengths
    p1 = len_dict[2][0]
    return_value[p1] = 1
    p4 = len_dict[4][0]
    return_value[p4] = 4
    return_value[len_dict[3][0]] = 7
    return_value[len_dict[7][0]] = 8
    p3 = None
    p5 = None
    for pattern in len_dict[5]:
        # 3 is the only length 5 digit that contains all the segments of 1
        if contains_all(p1, pattern):
            p3 = pattern
            return_value[p3] = 3
        else:
            overlap_count = overlap(pattern, p4)
            # 2 and 5 are distinguished by their overlap with 4
            if overlap_count == 3:
                p5 = pattern
                return_value[p5] = 5
            else:
                return_value[pattern] = 2
    for pattern in len_dict[6]:
        # Of the length 6 digits, only 9 contains all the segments of 3
        if contains_all(p3, pattern):
            return_value[pattern] = 9
        # 6 contains all the segments of 5
        elif contains_all(p5, pattern):
            return_value[pattern] = 6
        else:
            return_value[pattern] = 0

    return return_value


total_unique_patterns = 0
total_values = 0
with open('day8.txt', 'r') as f:
    for line in f:
        signal_pattern, output_value = line.rstrip().split(" | ")
        values = [sorted_str(s) for s in output_value.split(" ")]
        patterns = [sorted_str(s) for s in signal_pattern.split(" ")]
        counter = Counter([len(i) for i in values])
        total_unique_patterns += (counter[2] + counter[3] + counter[4] + counter[7])
        decoded = decode(patterns)
        decoded_value = 0
        for value in values:
            decoded_value = decoded_value * 10 + decoded[value]
        total_values += decoded_value

print("Part 1:", total_unique_patterns)
print("Part2:", total_values)
