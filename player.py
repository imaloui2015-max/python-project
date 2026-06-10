

# Create the tic tac to game so we create at first the platers that they well play the game

# the root class
class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game): # -> inhiretance
        pass

    
# create  childs class
class Humanplayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(self.letter + '\'s turn Input move (0, 9): ')
            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('Invalid square, pls try again a valid square')

        return val


import random
class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


import random
import math
# this class use a specific algorithm calls the minmax
class SmartComputer(Player):
    def __init__(self, letter):
        super().__init__(letter) # -> calls the root init

    def get_move(self, game):
        if len(game.available_move()) == 9:
            square = random.choice(game.available_move())

        else:
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.empty_square() + 1) if other_player == max_player else -1 * (state.empty_square() + 1) } 



        elif not state.empty_square():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {"position": None, 'score': -math.inf}

        else:
            best = {"position": None, 'score': math.inf}


        for possible_move in state.available_move():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

        
            state.border[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

