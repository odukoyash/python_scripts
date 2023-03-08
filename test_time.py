#!/usr/bin/python 

import time

time_string=time.localtime()
print(time_string)

TS=time.strftime("%m-%d-%Y-%M-%S",time_string)
print(TS)