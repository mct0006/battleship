# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:46:25 2016

@author: mct00
"""

##-------------------------------------------------
##
##      Ship Positions
##
##-------------------------------------------------

import random



class Positions(object):
    def __init__(self, name):
        self.name = name
        


    
    # Choose an initial orientation for each ship. 1 is horizontal, 2 is vertical.
    orient = (random.choice((1,2)), random.choice((1,2)), random.choice((1,2)), random.choice((1,2)), random.choice((1,2)))
        
        
    


    # Find the cells covered by "ship" givin its orientation k, size n,
    # and initial position with coordinates r_init, c_init. Prints the coordinates
    # of a ship as list [[r1, c1], [r2, c2],..., [rn, cn]].
    
    def position(self, k, n, r_init, c_init, ship):
        if k == 1:
            for i in range(n):
                ship.append([r_init, c_init + i])
        else:
            for i in range(n):
                ship.append([r_init + i, c_init])      
        return ship
    


    
    # Small procedure to guarantee that ships do not overlap.
    
    def overlap(self, s1, s2):
        counter = 0
        for j in range(len(s1)):
            for m in range(len(s2)):
                if s1[j] == s2[m]:
                    counter = counter + 1
        if counter > 0:
            return 1
        else:
            return 0

    # Randomly choose initial cell for each ship; this step will fix a ship's position, effectively preventing
    # it from being rerandomized unnecessarily. 

    s5o1r = random.randint(1,10)
    s5o1c = random.randint(1,6)
    s5o2r = random.randint(1,6)
    s5o2c = random.randint(1,10)
    s4o1r = random.randint(1,10)
    s4o1c = random.randint(1,7)
    s4o2r = random.randint(1,7)
    s4o2c = random.randint(1,10)
    s3_1o1r = random.randint(1,10)
    s3_1o1c = random.randint(1,8)
    s3_1o2r = random.randint(1,8)
    s3_1o2c = random.randint(1,10)
    s3_2o1r = random.randint(1,10)
    s3_2o1c = random.randint(1,8)
    s3_2o2r = random.randint(1,8)
    s3_2o2c = random.randint(1,10)
    s2o1r = random.randint(1,10)
    s2o1c = random.randint(1,9)
    s2o2r = random.randint(1,9)
    s2o2c = random.randint(1,10)


    def rerandomize(self, k, n):
        if k == 1:
            init_row = random.randint(1,10)
            init_col = random.randint(1,10-n+1)
        else:
            init_row = random.randint(1,10-n+1)
            init_col = random.randint(1,10)
        return (init_row, init_col)
    
    # Record positions of each ship.
    
    
    
    
    
    def s5_position(self):
        if self.orient[0] == 1:
            s5_init_row = self.s5o1r
            s5_init_col = self.s5o1c
            return self.position(self.orient[0], 5, s5_init_row, s5_init_col, [])
        else:
            s5_init_row = self.s5o2r
            s5_init_col = self.s5o2c
            return self.position(self.orient[0], 5, s5_init_row, s5_init_col, [])
    
  

    
    def s4_position(self):
        loop = 0
        while loop == 0:
            if self.orient[1] == 1:
                s4_init_row = self.s4o1r
                s4_init_col = self.s4o1c
                pos = self.position(self.orient[1], 4, s4_init_row, s4_init_col, [])
            else:
                s4_init_row = self.s4o2r
                s4_init_col = self.s4o2c
                pos = self.position(self.orient[1], 4, s4_init_row, s4_init_col, [])
            if self.overlap(self.s5_position(),pos) == 0:
                return pos
                loop = 1
            else:
                if self.orient[1] == 1:
                    self.s4o1r = self.rerandomize(1,4)[0]
                    self.s4o1c = self.rerandomize(1,4)[1]
                else:
                    self.s4o2r = self.rerandomize(2,4)[0]
                    self.s4o2c = self.rerandomize(2,4)[1]
    
          
   


    def s3_1_position(self):
        loop = 0
        while loop == 0:
            if self.orient[2] == 1:
                s3_1_init_row = self.s3_1o1r
                s3_1_init_col = self.s3_1o1c
                pos = self.position(self.orient[2], 3, s3_1_init_row, s3_1_init_col, [])
            else:
                s3_1_init_row = self.s3_1o2r
                s3_1_init_col = self.s3_1o2c
                pos = self.position(self.orient[2], 3, s3_1_init_row, s3_1_init_col, [])
            if self.overlap(self.s5_position(),pos) == 0 and self.overlap(self.s4_position(),pos)==0:
                return pos
                loop = 1
            else:
                if self.orient[2] == 1:
                    self.s3_1o1r = self.rerandomize(1,3)[0]
                    self.s3_1o1c = self.rerandomize(1,3)[1]
                else:
                    self.s3_1o2r = self.rerandomize(2,3)[0]
                    self.s3_1o2c = self.rerandomize(2,3)[1]
    
    


    def s3_2_position(self):
        loop = 0
        while loop == 0:
            if self.orient[3] == 1:
                s3_2_init_row = self.s3_2o1r
                s3_2_init_col = self.s3_2o1c
                pos = self.position(self.orient[3], 3, s3_2_init_row, s3_2_init_col, [])
            else:
                s3_2_init_row = self.s3_2o2r
                s3_2_init_col = self.s3_2o2c
                pos = self.position(self.orient[3], 3, s3_2_init_row, s3_2_init_col, [])
            if self.overlap(self.s5_position(),pos) == 0 and self.overlap(self.s4_position(),pos)==0 and self.overlap(self.s3_1_position(),pos)==0:
                return pos
                loop = 1
            else:
                if self.orient[3] == 1:
                    self.s3_2o1r = self.rerandomize(1,3)[0]
                    self.s3_2o1c = self.rerandomize(1,3)[1]
                else:
                    self.s3_2o2r = self.rerandomize(2,3)[0]
                    self.s3_2o2c = self.rerandomize(2,3)[1]



    
    def s2_position(self):
        loop = 0
        while loop == 0:
            if self.orient[4] == 1:
                s2_init_row = self.s2o1r
                s2_init_col = self.s2o1c
                pos = self.position(self.orient[4], 2, s2_init_row, s2_init_col, [])
            else:
                s2_init_row = self.s2o2r
                s2_init_col = self.s2o2c
                pos = self.position(self.orient[4], 2, s2_init_row, s2_init_col, [])
            if self.overlap(self.s5_position(),pos) == 0 and self.overlap(self.s4_position(),pos)==0 and self.overlap(self.s3_1_position(),pos)==0 and self.overlap(self.s3_2_position(),pos)==0:
                return pos
                loop = 1
            else:
                if self.orient[4] == 1:
                    self.s2o1r = self.rerandomize(1,2)[0]
                    self.s2o1c = self.rerandomize(1,2)[1]
                else:
                    self.s2o2r = self.rerandomize(2,2)[0]
                    self.s2o2c = self.rerandomize(2,2)[1]
                    
            





#---------------------------------------------------------------------------------------------------

#       Example of code that didn't work; it rerandomized the location of a ship each time it was called, 
#       instead of fixing the ship's position.

#---------------------------------------------------------------------------------------------------




#    def s4_position(self):
#        loop = 0
#        while loop == 0:
#            if self.orient[1] == 1:
#                s4_init_row = random.randint(1,10)
#                s4_init_col = random.randint(1,7)
#                pos = self.position(self.orient[1], 4, s4_init_row, s4_init_col, [])
#            else:
#                s4_init_row = random.randint(1,7)
#                s4_init_col = random.randint(1,10)
#                pos = self.position(self.orient[1], 4, s4_init_row, s4_init_col, [])
#            if self.overlap(self.s5_position(),pos) == 0:
#                return pos
#                loop = 1       