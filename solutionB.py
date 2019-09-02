#!/usr/bin/python

'''
Question B - The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
'''
import sys

class Compare_Version():

    #method to compare 2 string
    def compare(s1,s2):	
        #Input Validation 
        if "." not in s1:
            print ("ERROR !!!")			
            print ("First Input " + s1 + " doesn't seems to be a version string")
            print ("The version string should be in major.minor OR major.minor[.build[.revision]] OR major.minor[.build] format")	
            print("As an example:1.2 OR 1.2.1.2 OR 1.2.1")
            print ("Please profvide First input and try again")			
            sys.exit()
        elif "." not in s2:
            print ("ERROR !!!")					
            print ("Second Input " + s2 + " doesn't seems to be a version string")
            print ("The version string should be in major.minor OR major.minor[.build[.revision]] OR major.minor[.build] format")	
            print("As an example:1.2 OR 1.2.1.2 OR 1.2.1")
            print ("Please profvide First input and try again")			
            sys.exit()		
        #conditions		
        if s1 > s2:
            return chr(34) + s1 + chr(34) + " is greater than " + chr(34) + s2 + chr(34)
        elif s1 < s2:
            return chr(34) + s1 + chr(34) + " is less than " + chr(34) + s2 + chr(34)
        elif s1 == s2:			
            return chr(34) + s1 + chr(34) + " is equal to " + chr(34) + s2 + chr(34)