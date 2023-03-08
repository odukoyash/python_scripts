#!/usr/bin/python

#A MODULE IS A BODY OF CODE THAT HAS FUNCTIONS IN IT, A CLASS AN OBJECT THAT 

#Modules
#The shutils class has a functions in it which helps to copy files from a source to a destination

import shutil

#variable declaration
SOURCE="c:/apps/terraform/tf/stackit/practicedir_python/adenuga"
DESTINATION="c:/apps/terraform/tf/stackit/practicedir_jul22_shina"

#print("The SOURCE file is: {}, The DESTINATION file is: {}".format(SOURCE,DESTINATION) )

shutil.copy2(SOURCE,DESTINATION)


