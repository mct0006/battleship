import random
import time


##-------------------------------------------------
##
##      Initial Game Board
##
##-------------------------------------------------

board = [["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]]

for i in range(9):
    board.append([" "+str(i+1), "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",])
board.append([str(10), "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])
 
def print_board():
    for i in range(11):
        print(" ".join(board[i]))

##-------------------------------------------------
##
##      Alphabet to Number Dictionary
##
##-------------------------------------------------


alph = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}



        
##-------------------------------------------------
##
##      Initial Ship Positions
##
##-------------------------------------------------

# Choose an initial orientation for a ship. 1 is horizontal, 2 is vertical.
def orient():
    return random.choice((1,2))

s5_orient = orient()
s4_orient = orient()
s3_1_orient = orient()
s3_2_orient = orient()
s2_orient = orient()


# Find the cells covered by "ship" givin its orientation k, size n,
# and initial position with coordinates r_init, c_init. Prints the coordinates
# of a ship as list [[r1, c1], [r2, c2],..., [rn, cn]].

def position(k, n, r_init, c_init, ship):
    if k == 1:
        for i in range(n):
            ship.append([r_init, c_init + i])
    else:
        for i in range(n):
            ship.append([r_init + i, c_init])
            
    return ship


# Small procedure to guarantee that ships do not overlap.

def overlap(s1, s2):
    counter = 0
    for j in range(len(s1)):
        for m in range(len(s2)):
            if s1[j] == s2[m]:
                counter = counter + 1
    if counter > 0:
        return 1
    else:
        return 0
        



# Choose and record initial positions of each ship.

def s5_position():
    if s5_orient == 1:
        s5_init_row = random.randint(1,10)
        s5_init_col = random.randint(1,6)
        return position(s5_orient, 5, s5_init_row, s5_init_col, [])
    else:
        s5_init_row = random.randint(1,6)
        s5_init_col = random.randint(1,10)
        return position(s5_orient, 5, s5_init_row, s5_init_col, [])


s5_pos = s5_position()     


def s4_position():
    loop = 0
    while loop == 0:
        if s4_orient == 1:
            s4_init_row = random.randint(1,10)
            s4_init_col = random.randint(1,7)
            pos = position(s4_orient, 4, s4_init_row, s4_init_col, [])
        else:
            s4_init_row = random.randint(1,7)
            s4_init_col = random.randint(1,10)
            pos = position(s4_orient, 4, s4_init_row, s4_init_col, [])
        if overlap(s5_pos,pos) == 0:
            return pos
            loop = 1
        


s4_pos = s4_position()


def s3_1_position():
    loop = 0
    while loop == 0:
        if s3_1_orient == 1:
            s3_1_init_row = random.randint(1,10)
            s3_1_init_col = random.randint(1,8)
            pos = position(s3_1_orient, 3, s3_1_init_row, s3_1_init_col, [])
        else:
            s3_1_init_row = random.randint(1,8)
            s3_1_init_col = random.randint(1,10)
            pos = position(s3_1_orient, 3, s3_1_init_row, s3_1_init_col, [])
        if overlap(s5_pos,pos) == 0 and overlap (s4_pos,pos) == 0:
            return pos
            loop = 1
        


s3_1_pos = s3_1_position()

def s3_2_position():
    loop = 0
    while loop == 0:
        if s3_2_orient == 1:
            s3_2_init_row = random.randint(1,10)
            s3_2_init_col = random.randint(1,8)
            pos = position(s3_2_orient, 3, s3_2_init_row, s3_2_init_col, [])
        else:
            s3_2_init_row = random.randint(1,8)
            s3_2_init_col = random.randint(1,10)
            pos = position(s3_2_orient, 3, s3_2_init_row, s3_2_init_col, [])
        if overlap(s5_pos,pos) == 0 and overlap(s4_pos,pos) == 0 and overlap(s3_1_pos,pos) == 0:
            return pos
            loop = 1
        


s3_2_pos = s3_2_position()



def s2_position():
    loop = 0
    while loop == 0:
        if s2_orient == 1:
            s2_init_row = random.randint(1,10)
            s2_init_col = random.randint(1,9)
            pos = position(s2_orient, 2, s2_init_row, s2_init_col, [])
        else:
            s2_init_row = random.randint(1,9)
            s2_init_col = random.randint(1,10)
            pos = position(s2_orient, 2, s2_init_row, s2_init_col, [])
        if overlap(s5_pos,pos) == 0 and overlap(s4_pos,pos) == 0 and overlap(s3_1_pos,pos) == 0 and overlap(s3_2_pos,pos) == 0:
            return pos
            loop = 1
        


s2_pos = s2_position()




##print(s5_pos)
##print(s4_pos)
##print(s3_1_pos)
##print(s3_2_pos)
##print(s2_pos)
        
##-------------------------------------------------
##
##      Game Play
##
##-------------------------------------------------


print("Welcome to Battleship! Here is your gameboard:")


i = 0
while i < 60:
    print_board()
    c = 1
    while c > 0:
        while True:
            try:
                user_row = int(input("Choose a row number: "))
                break
            except (SyntaxError, ValueError):
                print("Please enter a valid row number!")
        if user_row in range(1,11):
            c = 0
        else:
            print("Please enter a valid row number!")
    while c < 1:
        while True:
            try:
                user_col = str(input("Choose a column letter: ")).upper()
                break
            except (SyntaxError, ValueError):
                print("Please enter a valid column letter!")
        if user_col in alph:
            c = 1
        else:
            print("Please enter a valid column letter!")
    guess = [user_row, alph[user_col]]

    

    if guess in s5_pos :
        print("You hit a ship!\n")
        board[user_row][alph[user_col]] = "X"
        s5_pos.remove(guess)
        if s5_pos == []:
            print("You sank my aircraft carrier!\n")
    elif guess in s4_pos:
        print("You hit a ship!\n")
        board[user_row][alph[user_col]] = "X"
        s4_pos.remove(guess)
        if s4_pos == []:
            print("You sank my battleship!\n")
    elif guess in s3_1_pos:
        print("You hit a ship!\n")
        board[user_row][alph[user_col]] = "X"
        s3_1_pos.remove(guess)
        if s3_1_pos == []:
            print("You sank my destroyer!\n")
    elif guess in s3_2_pos:
        print("You hit a ship!\n")
        board[user_row][alph[user_col]] = "X"
        s3_2_pos.remove(guess)
        if s3_2_pos == []:
            print("You sank my submarine!\n")
    elif guess in s2_pos:
        print("You hit a ship!\n")
        board[user_row][alph[user_col]] = "X"
        s2_pos.remove(guess)
        if s2_pos == []:
            print("You sank my patrol boat!\n")
    else:
        print("You missed.\n")
        board[user_row][alph[user_col]] = "."
    time.sleep(1)
    if s5_pos == [] and s4_pos == [] and s3_1_pos == [] and s3_2_pos == [] and s2_pos == []:
        print("You sank all of my ships! You won the game!")
        i = 60
    elif i == 59:
        print("You lost!")
    i = i + 1


