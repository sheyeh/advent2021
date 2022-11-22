import itertools


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

    def roll(self, value):
        self.position = (self.position + value - 1) % 10 + 1
        self.score += self.position

    def play(self, die):
        self.roll(die.roll() + die.roll() + die.roll())

    def win(self, winning_score):
        return self.score >= winning_score

    def unroll(self, value):
        self.score -= self.position
        self.position = (self.position - value - 1) % 10 + 1

    def __str__(self):
        return "position: {}, score: {}".format(self.position, self.score)


dice_possibilities = {}
for x, y, z in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
    dice_possibilities.setdefault(x + y + z, 0)
    dice_possibilities[x + y + z] += 1


def split(players, turn=0, depth=0):
    wins = [0, 0]
    player = players[turn]
    for rolled in dice_possibilities:
        player.roll(rolled)
        if player.win(21):
            wins[turn] += dice_possibilities[rolled]
        else:
            new_players = players
            new_players[turn] = player
            next_wins = split(new_players, (turn + 1) % 2, depth+1)
            wins[0] += next_wins[0] * dice_possibilities[rolled]
            wins[1] += next_wins[1] * dice_possibilities[rolled]
        player.unroll(rolled)
    return wins


deterministic_die = Die()
the_players = [Player(7), Player(9)]
player_number = 0
while True:
    the_players[player_number].play(deterministic_die)
    if the_players[player_number].win(1000):
        break
    player_number = (player_number + 1) % 2

print("Part 1", deterministic_die.count * min(the_players[0].score, the_players[1].score))
the_players = [Player(7), Player(9)]
wins = split(the_players)
print("Part 2:", max(wins))
