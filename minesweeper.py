import re 
import random


class Board:
    def __init__(self, dim_size, num_boms):
        self.dim_size = dim_size
        self.num_boms = num_boms

        self.border = self.make_border()
        self.assign_values_to_border()

        self.dug = set()


    def make_border(self,):

        border = [[None for i in range(self.dim_size)] for _ in range(self.dim_size)] # -> thats create an array of None 10*10

        # plant the boms
        boms_plated = 0
        while boms_plated < self.num_boms:
            loc = random.randint(0, self.dim_size**2 - 1)
            row  = loc // self.dim_size # we want to know the row of the boms
            col = loc % self.dim_size # we want to knwo the col of the boms

            if border[row][col] == '*':
                # -> we want to know if it's already exist
                continue

            border[row][col] = '*'
            boms_plated += 1
        return border

    def assign_values_to_border(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.border[r][c] == '*':
                    continue
                self.border[r][c] = self.get_num_neighbore_boms(r, c) # -> we want to give a number based on num of the neighbor boms

    
    def get_num_neighbore_boms(self, row, col):
        # top_left -> (row - 1, col - 1)
        # top_midel -> (row -1 , col)
        # top_right -> (row - 1, col + 1)
        # left -> (row , col - 1)
        # right -> (row, col + 1)
        # button_left -> (row + 1, col - 1)
        # bottom_right -> (row + 1, col + 1)


        num_get_num_neighbore_boms = 0

        for r in range(max(0, row-1), min(self.dim_size - 1, row+2)): # the way why we impliment the max and the min is bc smtimes we must look at the neighbore top that gonna be -1 or 0 if it's in the buttom
            for c in range(max(0, col-1), min(self.dim_size - 1, col+2)):
                if r == row and c == col:
                    continue
                if self.border[r][c] == '*':
                    num_get_num_neighbore_boms += 1

        return num_get_num_neighbore_boms

    def dig(self, row, col):
        
        self.dug.add((row, col))

        if self.border[row][col] == '*':
            return False
        
        elif self.border[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size - 1, row+2)): # the way why we impliment the max and the min is bc smtimes we must look at the neighbore top that gonna be -1 or 0 if it's in the buttom
            for c in range(max(0, col-1), min(self.dim_size - 1, col+2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c) # -> Recursion

        return True


    def __str__(self):
        visible_border = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_border = str(self.border[row][col])

                else:
                    visible_border[row][col] = ' '

        
        string_rep = ' '

        widths = []

        for index in range(self.dim_size):
            columns = map(lambda x: x[index], visible_border)

   
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []

        for index, col in enumerate(indices):
            format = '%-' + str(widths[index]) + "s"
            cells.append(format % (col))

        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_border)):
            row = visible_border[i]
            string_rep += f'{i}  |'
            cells = []
            for index, col in enumerate(row):               
                format = '%-' + str(widths[index]) + "s"
                cells.append(format % (col))

                string_rep += ' |'.join(cells)
                string_rep += ' |\n'

            
            str_len = int(len(string_rep) / self.dim_size)
            string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

            return string_rep

        

def play_game(dim_size=10, num_boms=10):
    border = Board(dim_size, num_boms)

    safe = True

    while len(border.dug) < border.dim_size**2 - num_boms:
        print(border)

        user_input = re.split(',(\\s)*', input("Where whould you like to dig?, Input row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= border.dim_size or col < 0 or col >= border.dim_size:
            print("Invalid location. pls try agein")
            continue

        safe = border.dig(row,col)

        if not safe:
            break

        if safe:
            print("congratulation you win 100000000 dollar")
        else:
            print("GAME OVER!!!!!")
            border.dug = [(r,c) for r in range(border.dim_size) for c in range(border.dim_size)]
            print(border)




if __name__ == '__main__':
    play_game()

                



