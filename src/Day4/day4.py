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

done = False
for draw in draws:
    for board in boards:
        board.mark(draw)
        if board.winner:
            print("Part 1:", board.sum * int(draw))
            done = True
            break
    if done:
        break
