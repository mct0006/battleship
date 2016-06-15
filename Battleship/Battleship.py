# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:58:11 2016

@author: mct00
"""

import random
import time
from InitialBoard import Board
from ShipPositions import Positions


##-------------------------------------------------
##
##      Tools for AI Component
##
##-------------------------------------------------








##-------------------------------------------------
##
##      Alphabet to Number Dictionary
##
##-------------------------------------------------


alph = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}

 
##-------------------------------------------------
##
##      Procedure to Automate Computer Guesses
##
##-------------------------------------------------




def smart_guess(x):
    temp_guess_list = []
    if len(x) == 1:
        a = x[0][0]
        b = x[0][1]
        if not [a+1,b] in c_guess_list and a+1 < 11:
            temp_guess_list.append([a+1,b])
        if not [a-1,b] in c_guess_list and a-1 >0:
            temp_guess_list.append([a-1,b])
        if not [a,b+1] in c_guess_list and b+1 < 11:
            temp_guess_list.append([a,b+1])
        if not [a,b-1] in c_guess_list and b-1 > 0:
            temp_guess_list.append([a,b-1])    
    else:
        if x[0][0] == x[1][0]: #horizontal
            a = min(x)[1]
            b = max(x)[1]
            if a == b-1:
                if not [x[0][0],b+1] in c_guess_list and b+1 < 11:
                    temp_guess_list.append([x[0][0],b+1])
                if not [x[0][0],a-1] in c_guess_list and a-1 > 0:
                    temp_guess_list.append([x[0][0],a-1])
            else:
                counter = 1
                for k in range(a+1,b):
                    if [x[0][0],k] in c_guess_list:
                        counter = counter + 1
                if counter == b - a:    
                    if not [x[0][0],b+1] in c_guess_list and b+1 < 11:
                        temp_guess_list.append([x[0][0],b+1])
                    if not [x[0][0],a-1] in c_guess_list and a-1 > 0:
                        temp_guess_list.append([x[0][0],a-1])
                else:
                    for k in range(a+1,b):
                        if not [x[0][0],k] in c_guess_list:
                            temp_guess_list.append([x[0][0],k])
                
        else:                 #vertical
            a = min(x)[0]
            b = max(x)[0]
            if a == b-1:
                if not [b+1,x[0][1]] in c_guess_list and b+1 < 11:
                    temp_guess_list.append([b+1,x[0][1]])
                if not [a-1,x[0][1]] in c_guess_list and a-1 > 0:
                    temp_guess_list.append([a-1,x[0][1]])
            else:
                counter = 1
                for k in range(a+1,b):
                    if [k,x[0][1]] in c_guess_list:
                        counter = counter + 1
                if counter == b - a:    
                    if not [b+1,x[0][1]] in c_guess_list and b+1 < 11:
                        temp_guess_list.append([b+1,x[0][1]])
                    if not [a-1,x[0][1]] in c_guess_list and a-1 > 0:
                        temp_guess_list.append([a-1,x[0][1]])
                else:
                    for k in range(a+1,b):
                        if not [k,x[0][1]] in c_guess_list:
                            temp_guess_list.append([k,x[0][1]])
    r = random.randint(0,len(temp_guess_list)-1)
    return temp_guess_list[r]       



        
##-------------------------------------------------
##
##      Game Play
##
##-------------------------------------------------

p_board = Board("Your Gameboard:")
p_ships = Positions("Ships on Your Board:")
c_board = Board("Your Opponent's Gameboard:")
c_ships = Positions("Ships on Your Opponent's Board:")

p_board.setup()
c_board.setup()

p5ship = p_ships.s5_position()
p4ship = p_ships.s4_position()
p3_1ship = p_ships.s3_1_position()
p3_2ship = p_ships.s3_2_position()
p2ship = p_ships.s2_position()
c5ship = c_ships.s5_position()
c4ship = c_ships.s4_position()
c3_1ship = c_ships.s3_1_position()
c3_2ship = c_ships.s3_2_position()
c2ship = c_ships.s2_position()






print("Welcome to Battleship!")

print(p_board.name)
p_board.print_board()
print("\n")
print(c_board.name)
c_board.print_board()


p_guess_list = []
c_guess_list = []
c_hit_tracker = [[],[],[],[],[]]




game_loop = 0
while game_loop == 0:
    
    #### Human Turn
    
    
    print("\n")    
    print("It's your turn!")
    c = 1
    g = 0
    while g == 0:
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
        if [user_row, alph[user_col]] in p_guess_list:
            print("You've already guessed that location!")
        else:
            guess = [user_row, alph[user_col]]
            p_guess_list.append(guess)
            g = 1
            
    

    if guess in p5ship:
        print("You hit one of my ships!\n")
        p_board.init[user_row][alph[user_col]] = "X"
        p5ship.remove(guess)
        if p5ship == []:
            print("You sank my aircraft carrier!\n")
    elif guess in p4ship:
        print("You hit a ship!\n")
        p_board.init[user_row][alph[user_col]] = "X"
        p4ship.remove(guess)
        if p4ship == []:
            print("You sank my battleship!\n")
    elif guess in p3_1ship:
        print("You hit a ship!\n")
        p_board.init[user_row][alph[user_col]] = "X"
        p3_1ship.remove(guess)
        if p3_1ship == []:
            print("You sank my destroyer!\n")
    elif guess in p3_2ship:
        print("You hit a ship!\n")
        p_board.init[user_row][alph[user_col]] = "X"
        p3_2ship.remove(guess)
        if p3_2ship == []:
            print("You sank my submarine!\n")
    elif guess in p2ship:
        print("You hit a ship!\n")
        p_board.init[user_row][alph[user_col]] = "X"
        p2ship.remove(guess)
        if p2ship == []:
            print("You sank my patrol boat!\n")
    else:
        print("You missed.\n")
        p_board.init[user_row][alph[user_col]] = "."
    if p5ship == [] and p4ship == [] and p3_1ship == [] and p3_2ship == [] and p2ship == []:
        print("You win!")
        game_loop = 1
        break
    p_board.print_board()
    time.sleep(1)
    
    
    
    #### Computer Turn
    
    

    print("\n")
    print("It's my turn.")
    time.sleep(1)
    
    c = 1
    while c == 1:  
        if c_hit_tracker == [[],[],[],[],[]]:
            guess = [random.randint(1,10),random.randint(1,10)]
            while guess in c_guess_list:
                guess = [random.randint(1,10),random.randint(1,10)]
            c = 0  
        elif not c_hit_tracker[0] == []:
            guess = smart_guess(c_hit_tracker[0])
            c = 0
        elif not c_hit_tracker[1] == []:
            guess = smart_guess(c_hit_tracker[1])
            c = 0
        elif not c_hit_tracker[2] == []:
            guess = smart_guess(c_hit_tracker[2])
            c = 0
        elif not c_hit_tracker[3] == []:
            guess = smart_guess(c_hit_tracker[3])
            c = 0
        elif not c_hit_tracker[4] == []:
            guess = smart_guess(c_hit_tracker[4])
            c = 0
        
        
    c_guess_list.append(guess)
    
    if guess in c5ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c5ship.remove(guess)
        c_hit_tracker[0].append(guess)
        if c5ship == []:
            print("I sank your aircraft carrier!\n")
            c_hit_tracker[0] = []
    elif guess in c4ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c4ship.remove(guess)
        c_hit_tracker[1].append(guess)
        if c4ship == []:
            print("I sank your battleship!\n")
            c_hit_tracker[1] = []
    elif guess in c3_1ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c3_1ship.remove(guess)
        c_hit_tracker[2].append(guess)
        if c3_1ship == []:
            print("I sank your destroyer!\n")
            c_hit_tracker[2] = []
    elif guess in c3_2ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c3_2ship.remove(guess)
        c_hit_tracker[3].append(guess)
        if c3_2ship == []:
            print("I sank your submarine!\n")
            c_hit_tracker[3] = []
    elif guess in c2ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c2ship.remove(guess)
        c_hit_tracker[4].append(guess)
        if c2ship == []:
            print("I sank your patrol boat!\n")
            c_hit_tracker[4] = []
    else:
        print("I missed.")
        c_board.init[guess[0]][guess[1]] = "."
    if c5ship == [] and c4ship == [] and c3_1ship == [] and c3_2ship == [] and c2ship == []:
        print("I sank all of your ships! You lose.")
        game_loop = 1
    else: 
        c_board.print_board()    
    
    
 
    time.sleep(1)
print("Thanks for playing!")






