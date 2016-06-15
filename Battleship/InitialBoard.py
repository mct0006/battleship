# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:41:14 2016

@author: mct00
"""

##-------------------------------------------------
##
##      Initial Game Board
##
##-------------------------------------------------

class Board(object):
    def __init__(self, name):
        self.name = name
        self.init = [["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]]
        
    def setup(self):
        for i in range(9):
            self.init.append([" "+str(i+1), "O", "O", "O", "O", "O", "O", "O", "O", "O", "O",])
        self.init.append([str(10), "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])
        
 
    def print_board(self):
        for i in range(11):
            print(" ".join(self.init[i]))

