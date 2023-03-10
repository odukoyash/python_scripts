#!/usr/bin/python

import sys,os
'''
#the name of the script is the first command line argument, threeshold is the second command line arg
if (len(sys.argv)) != 2:
    print("You entered the wrong number of command line argument")
    exit()
else:
    threshold=sys.argv[1]
    print("You entered the threshold of {}".format(threshold))

#raw_input() function, which is not available in Python 3, instead use input
#entry=int(input("Enter disk utilzation threshold: "))
#print('You enter {}'.format(entry))
'''
#opening a file 
#creating a variable called fh file handler and it could be any
#w+ means you can write into the file after opening it
fh=open("shina_america.par","w+")
fh.write("I love being a cloud engineer")
fh.close()

fh=open("shina_america.par","r+")
file_content=fh.read()
print(file_content)
fh.close()

list=os.listdir('.')
print(list)


