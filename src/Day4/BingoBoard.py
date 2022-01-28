import math


class BingoBoard:
    def __init__(self, numbers):
        n = int(math.sqrt(len(numbers)))
        assert n * n == len(numbers)
        self.N = n
        self.numbers = numbers
        self.sum = sum(int(num) for num in numbers)
        self.row_hits = [0] * self.N
        self.col_hits = [0] * self.N
        self.pos = {}
        for i in range(0, len(numbers)):
            num = numbers[i]
            self.pos[num] = (i % n, int(i / n))
        self.winner = False

    def winner(self):
        return self.winner

    def mark(self, num):
        pos = self.pos.get(num)
        if pos:
            self.sum -= int(num)
            self.row_hits[pos[0]] += 1
            self.col_hits[pos[1]] += 1
            if self.row_hits[pos[0]] == self.N or self.col_hits[pos[1]] == self.N:
                self.winner = True
