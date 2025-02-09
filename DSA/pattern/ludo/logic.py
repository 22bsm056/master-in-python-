class Game:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = {i: {'tokens': [0] * 4} for i in range(1, num_players + 1)}
        self.current_turn = 1

    def roll_dice(self):
        return random.randint(1, 6)

    def move_token(self, player, token_index, steps):
        if 0 <= token_index < 4:
            self.players[player]['tokens'][token_index] += steps

    def next_turn(self):
        self.current_turn = (self.current_turn % self.num_players) + 1
