#!/usr/bin/python

#note commands module is deprecated and has been removed in Python 3. Instead, you should use the subprocess module, which provides more functionality and is more secure.
import random
import subprocess 
import logging
import time

"""
#Variable Declaration
x="stupid"

def test_global():
    global x
    x="fantastic"
    print("python is : %s"%(x))

test_global()

print("Python is %s"%(x))

#check the data type of a variable
print(type (x))

#create turple
check_tuple=("Amaka", "Glenda", "Nevasha", "Afolabi", "Ayotunde")
print(check_tuple)

print(check_tuple[4])

fruit_list=["grapes", "pineapple", "mango"]
print(fruit_list[2])


#creating dictionary
student={
    "student_first_name":"tom",
    "student_last_name":"smith",
    "gender":"Male"
    }
print(student)

#lookings
for x in student:
    print(x)

for x in student:
    print(student[x])

print(student["student_first_name"])
print(student["student_last_name"])
print(student["gender"])

cars={
    "brand":{"Main_brand":"audi","sub_brand":"porsche"},
    "model":"panamera",
    "year":"1964",
}
print(cars)

word="python"
print(word[0])
print(word[-1])
print(word[-2])
print(word[-3])
print(word[2])
"""
#start time logging
#The purpose of this logging is to log into a file, you can log INFO, DEBUG,CRITICAL, WARNING
#filemodde w overrides the files everything it runs
#format what the message looks
#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
#logging.basicConfig(filename='dictionary_hostname_logging.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.CRITICAL)
#logging.basicConfig(level=logging.WARNING)
time_string=time.localtime()
TS=time_string = time.strftime("%m-%d-%y-%H:%M:%S")

logging.info("Starting code run at %s"%(TS))




hostname=subprocess.getoutput('hostname')
logging.info ("The hostname is %s"%(hostname))

servers={
    "DESKTOP-A9DN2BK":"pathprod)"
}

def patchprod():
    logging.info("This is the patchprod function")

for hostname in servers:
    if hostname=="DESKTOP-A9DN2BK":
        logging.info("Calling the "+servers["DESKTOP-A9DN2BK"]+" function")
        logging.info("Calling the "+servers[hostname]+" function")
    else:
        logging.error("SERVER NOT FOUND")

time_string=time.localtime()
TS=time_string = time.strftime("%m-%d-%y-%H:%M:%S")
logging.info("Ending code run at %s"%(TS))


    