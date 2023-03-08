#!/usr/bin/bash

#sys module to take command line arguement
#Module
import sys
x=sys.argv[1]
y=sys.argv[2]


print("The first command  line argument is: {}, The second command line arguement is: {}".format(x,y,) )

#function definition
#function: if statement 

def scheduled():
    print("The scheduled function has been called")

def unscheduled():
    prinyt("The unscheduled function has been called")

if x =="scheduled":
    print("Calling the scheduled funcntions")
    scheduled()
else:
    print("Calling the unscheduled functions")


