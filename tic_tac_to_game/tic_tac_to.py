
import math
import time
from player import Humanplayer, RandomComputer, SmartComputer




class TicTacTo():
    def __init__(self):
        self.border = self.make_border()
        self.current_winner = None


    @staticmethod
    def make_border():
        return [' ' for _ in range(9)]


    def print_border(self):
        for row in  [self.border[(i*3):(i+1)*3] for i in range(3)]:
            print(' |  +  | '.join(row) + ' |' )


    @staticmethod
    def border_num():
        number_border = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]

        for row in number_border:
            print(' |  +  | '.join(row) + ' |' )


    def make_move(self, square, letter):
        if self.border[square] == ' ':
            self.border[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False


    def winner(self, square, letter):
        row_ind = math.floor(square/3)
        row = self.border[row_ind*3:(row_ind+1)*3]

        if all(s == letter for s in row):
            return True

        col_ind = square % 3
        col = [self.border[col_ind+i*3] for i in range(3)]

        if all(s == letter for s in col):
            return True

        if square % 2 == 0:
            diag1 = [self.border[i] for i in [0, 4, 8]]

            if all(s == letter for s in diag1):
                return True

            diag2 = [self.border[i] for i in [2, 4, 6]]

            if all(s == letter for s in diag2):
                return True

        return False

    def empty_square(self):
        return ' ' in self.border

    def empty_square_num(self):
        return self.border.count(' ')

    def available_move(self):
        return [i for i, x in enumerate(self.border) if x == ' ']

    
def play_game(game, x_player, o_player, print_game=True):


    if print_game:
        game.border_num()

    letter = 'X'
    while game.empty_square():
        if letter == 'O':
            square = o_player.get_move(game)

        else:
            square = x_player.get_move(game)

        
        if game.make_move(square, letter):

            if print_game:
                print(letter + 'make a move to a square {}'.format(square))
                game.print_border()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!!!!")
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(4)

    if print_game:
        print("it's a tieee")


if __name__ == '__main__':
    x_player = Humanplayer('X')
    o_player = SmartComputer('O')
    t = TicTacTo()

    play_game(t, x_player, o_player, print_game=True)




            




