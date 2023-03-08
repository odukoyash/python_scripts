#!/usr/bin/python

#module importation
import os
import sys
import shutil

SRC=sys.argv[1]
DST=sys.argv[2]

def file_copy():
    print("CALLING THE FILE COPY FUNCTIONS")

shutil.copy(SRC,DST)
print("COPYING A FILE INTO A DESTINATION DIRECTORY")