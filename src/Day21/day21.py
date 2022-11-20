class Die:
    def __init__(self):
        self.outcome = 0
        self.count = 0

    def roll(self):
        self.outcome = self.outcome % 100 + 1
        self.count += 1
        return self.outcome


class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0

    def play(self, die):
        dice = die.roll() + die.roll() + die.roll()
        self.position = (self.position + dice - 1) % 10 + 1
        self.score += self.position

    def win(self):
        return self.score >= 1000


die = Die()
player = [Player(7), Player(9)]
player_number = 0
while True:
    player[player_number].play(die)
    if player[player_number].win():
        break
    player_number = (player_number + 1) % 2

print(die.count * min(player[0].score, player[1].score))
