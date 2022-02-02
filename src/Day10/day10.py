import re
import bisect

regex = re.compile(r'\[\]|\{\}|\<\>|\(\)')
corrupted = re.compile(r'\]|\}|\>|\)')


def score(line0):
    _syntax_error_score = 0
    _autocomplete_score = 0
    while regex.search(line0):
        line0 = re.sub(regex, "", line0)
    corrupted_match = corrupted.search(line0)
    if corrupted_match:
        _syntax_error_score += {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }[corrupted_match.group()]
    else:
        for c in reversed(line0):
            _autocomplete_score = _autocomplete_score * 5 + {
                 '(': 1,
                 '[': 2,
                 '{': 3,
                 '<': 4
             }[c]
    return _syntax_error_score, _autocomplete_score


total_syntax_error_score = 0
autocomplete_scores = []
with open('day10.txt', 'r') as f:
    for line in f:
        syntax_error_score, autocomplete_score = score(line.rstrip())
        total_syntax_error_score += syntax_error_score
        if autocomplete_score:
            bisect.insort(autocomplete_scores, autocomplete_score)

print("Part 1:", total_syntax_error_score)
print("Part 2:", autocomplete_scores[int(len(autocomplete_scores) / 2)])
