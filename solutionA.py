#!/usr/bin/python

'''
Question A - Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
'''

import sys
import types

class Overlap():

# Method that accepts two lines on x-axis and checks overlap
    def overlap_check(x1,x2,x3,x4):

        #print help/instructions	
        print ('\n\n' + "Please pass x1,x2,x3,x4 input/parameters as positive OR Negative integers to overlap_check method/Function" + '\n')

        #Input Validation 		
        if type(x1) != int:
            print ("x1 :" + str(x1) + " parameter is not a integer.")
            sys.exit()
        elif type(x2) != int:
            print ("x2 :" + str(x2) + " parameter is not a integer.")
            sys.exit()
        elif type(x3) != int:
            print ("x3 :" + str(x3) + " parameter is not a integer.")
            sys.exit()	
        elif type(x4) != int:
            print ("x4 :" + str(x4) + " parameter is not a integer.")
            sys.exit()

        #converting x1,x2 and x3,x4 into tuple respectively			  
        line1 = (x1,x2)
        line2 = (x3,x4)	
        flag = False
        result = str(line1) + " & " + str(line2) + " don't overlaps on x-axis"

        for i in range(2):
        # Checking -ve integers
            if line1[i] < 0 and line2[i] < 0:
                while 0 < len(line1) and not flag:
                    if line2[0] >= line1[0] or line2[0] >= line1[1]:
                        flag = True
                        result = str(line1) + " & " + str(line2) + " overlaps on x-axis"
                    break  
        # Checking +ve integers
            else:
                while 0 < len(line1) and not flag:
                    if line2[0] <= line1[0] or line2[0] <= line1[1]:
                        flag = True
                        result = str(line1) + ' & ' + str(line2) + ' overlaps on x-axis'
                    break   				
        return result