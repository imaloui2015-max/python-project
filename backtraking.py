

#### bACKTRACKING

#-> State backtracking ask to find a valid static by checking all the possiblity (N-queez, sudoko)


# solving the sudoko (bc it uses the recursion and the backtraking)


### AT THE FIRST WE DO A SERIE OF CHECKS TO SEE IF THE POSITION VALID OR NOT BASED ON THE CONTRAINST
def validation(r, c, n):

  for i in range(len(border)):
    if border[r][i] == n:
      return False
  return True

  for i in range(len(border)):
    if border[i][c] == n:
      return False
  return True

  box_r = (r // 3) * 3 # THAT RETURNS THE FIRST ELEMENT IN THE SUDOKO SQUARE ROW
  box_c = (c // 3) * 3 # THANT RETURNS THE FIRST ELEMENT IN THE SUDOKO SQUARE COLUMNS WE NEED THAT TO CHECK IF OUR N IS IN THE SQURE OR NOT BC IT4S ONE OF THE CONTRAINST

  for r in range(box_r, box_r + 3):
    for c in range(box_c, box_c + 3):
      if border[r][c] == n:
        return False
  return True
# THIS IS ANOTHER WAY TO DO IT
#def validation(r, c, n, border):
 # if n in border[r]:
  #  return False

  #col = [border[i][c] for i in range(9)]
  #if n in col:
    #return False

  #box_r = (r // 3) * 3
  #box_c = (c // 3) * 3

  #for r in range(box_r, box_r + 3):
    #for c in range(box_c, box_c + 3):
      #if border[r][c] == n:
        #return False
  #return True

# CHECK IF THERE STILL EMPTY SQUARZE
def search_for_empty(border):
  for r in range(9):
    for c in range(9):
      if border[r][c] == ".":
        return r, c
  return None, None


# AND THEN SOLVE THE GAME BY USING THOSE HELPER FUNVTION THAT WE'VE CREATED RN
def solve_sudoko(border):
  r, c = search_for_empty(border)

  if r == None:
    return True

  for n in range(1, 10):
    if validation(r, c, str(n), border):
      border[r][c] == str(n)
      if solve_sudoko(border):
        return True
      border[r][c] = "."
  return False

solve_sudoko(border)
print(border)