# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:13:44 2016

@author: mct00


"""

import random 
from ShipPositions import Positions
from InitialBoard import Board

c_board = Board("Your Opponent's Gameboard:")
c_board.setup()
c_ships = Positions("Ships on Your Opponent's Board:")
c5ship = c_ships.s5_position()
c4ship = c_ships.s4_position()
c3_1ship = c_ships.s3_1_position()
c3_2ship = c_ships.s3_2_position()
c2ship = c_ships.s2_position()


print(c_ships.s5_position())
print(c_ships.s4_position())
print(c_ships.s3_1_position())
print(c_ships.s3_2_position())
print(c_ships.s2_position())


c_guess_list = []
c_hit_tracker = [[],[],[],[],[]]

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


game_loop = 0
while game_loop == 0:
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
    
