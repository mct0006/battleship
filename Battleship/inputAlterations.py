# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:01:21 2016

@author: mct00
"""
alph = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
p_guess_list = []

##------------------------------------------------------------

c = 1
while c > 0:
    user_input = input("Choose a location: ")
    while True:
        try:
            user_row = int(user_input[1:])
            break
        except (SyntaxError, ValueError):
            print("Please enter a valid location!")
        if user_row in range(1,11):
        
print(user_row+3)

#print("\n")    
#    print("It's your turn!")
#    c = 1
#    g = 0
#    while g == 0:
#        while c > 0:
#            while True:
#                try:
#                    user_row = int(input("Choose a row number: "))
#                    break
#                except (SyntaxError, ValueError):
#                    print("Please enter a valid row number!")
#            if user_row in range(1,11):
#                c = 0
#            else:
#                print("Please enter a valid row number!")
#        while c < 1:
#            while True:
#                try:
#                    user_col = str(input("Choose a column letter: ")).upper()
#                    break
#                except (SyntaxError, ValueError):
#                    print("Please enter a valid column letter!")
#            if user_col in alph:
#                c = 1
#            else:
#                print("Please enter a valid column letter!")
#        if [user_row, alph[user_col]] in p_guess_list:
#            print("You've already guessed that location!")
#        else:
#            guess = [user_row, alph[user_col]]
#            p_guess_list.append(guess)
#            g = 1
    