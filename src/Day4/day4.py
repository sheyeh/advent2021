from src.Day4.BingoBoard import BingoBoard

boards = []
numbers = []
with open('day4.txt', 'r') as f:
    for line in f:
        if "," in line:
            draws = line.rstrip().split(",")
        if " " in line:
            numbers.extend(line.rstrip().split())
        if line == "\n" and numbers:
            boards.append(BingoBoard(numbers))
            numbers = []
    # handle last line
    boards.append(BingoBoard(numbers))

part_1 = 0
for draw in draws:
    for board in boards:
        if not board.winner:
            board.mark(draw)
            if board.winner:
                part_2 = board.sum * int(draw)  # keep score of last winning board
                if not part_1:  # first winning board
                    part_1 = part_2

print("Part 1:", part_1)
print("Part 2:", part_2)
