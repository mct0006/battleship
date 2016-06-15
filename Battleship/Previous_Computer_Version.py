# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:00:38 2016

@author: mct00
"""

###### Previous version of Computer Play






    while c == 1:  
        if c_hit_tracker = {}:
            guess = [random.randint(1,10),random.randint(1,10)]
            while guess in c_guess_list:
                guess = [random.randint(1,10),random.randint(1,10)]
    
   
    
    
    
    
    
    
    
    
    
    
    if guess in c5ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c5ship.remove(guess)
        if c5ship == []:
            print("I sank your aircraft carrier!\n")
    elif guess in c4ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c4ship.remove(guess)
        if c4ship == []:
            print("I sank your battleship!\n")
    elif guess in c3_1ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c3_1ship.remove(guess)
        if c3_1ship == []:
            print("I sank your destroyer!\n")
    elif guess in c3_2ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c3_2ship.remove(guess)
        if c3_2ship == []:
            print("I sank your submarine!\n")
    elif guess in c2ship:
        print("I hit one of your ships!\n")
        c_board.init[guess[0]][guess[1]] = "X"
        c2ship.remove(guess)
        if c2ship == []:
            print("I sank your patrol boat!\n")
    else:
        print("I missed.")
        c_board.init[guess[0]][guess[1]] = "."
    if c5ship == [] and c4ship == [] and c3_1ship == [] and c3_2ship == [] and c2ship == []:
        print("I sank all of your ships! You lose.")
        game_loop = 1
    else: 
        c_board.print_board()




