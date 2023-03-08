#!/usr/bin/python

#USER STORY: As a Cloud Engineer, I want to be able to pass command line arguments to backup files or directory
#ACCEPTANCE CRITERAL: Given that I am a Cloud Engineer, when i pass my command line argument, i should be able to backup files or directory

import shutil
import sys
import os

#Command line argument
SOURCE=sys.argv[1]
DESTINATION=sys.argv[2]
SOURCE_TYPE=sys.argv[3]

print("The first command line arguement is:{}".format(SOURCE) )
print("The second command line arguement is:{}".format(DESTINATION) )
print("The third command line arguement is:{}".format(SOURCE_TYPE) )


def file_copy():
    print("This is the file copy function")
    shutil.copy(SOURCE,DESTINATION)

def directory_copy():
    print("This is the directory copy function")
    shutil.copytree(SOURCE,DESTINATION)

if SOURCE =="F":
    print("CALLING THE FILE COPY FUNCTION")
elif DESTINATION =="D":
    print("CALLING THE DIRECTORY COPY FUNCTION")






