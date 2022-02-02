import re

regex = re.compile(r'\[\]|\{\}|\<\>|\(\)')
corrupted = re.compile(r'\]|\}|\>|\)')


def score(line0):
    _score = 0
    while regex.search(line0):
        line0 = re.sub(regex, "", line0)
    corrupted_match = corrupted.search(line0)
    if corrupted_match:
        _score += {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }[corrupted_match.group()]
    return _score


total_score = 0
with open('day10.txt', 'r') as f:
    for line in f:
        total_score += score(line.rstrip())

print(total_score)
