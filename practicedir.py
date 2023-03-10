#!/usr/bin/python
import sys,os   

'''
def check_word():
    a="Hello Cloud Engineer"
    if a[0]=='H':
    #if a[1:]=='H':
        print("The first letter of the word is: {}".format(a[0]))
    else:
        print("The rest letter of the words: {}".format(a[1:]))

check_word()


for x in os.listdir('.'):
    if x == "practicedir.log":
        print("The log file is: {}".format(x))
        logfile=open("%s"%x, "r+")
        file_content=logfile.read()
        print(file_content)
        logfile.close

        

threshold="85%"
threshold=threshold.replace('%','')
print(threshold)
threshold="95%"
threshold=threshold.strip('%')
print(threshold)

#to replace
a="SHINKOMAN"
print(a.lower())

a="shinkomana"
print(a.lower())




#i want to change the content of a file

fh=open("practicedir.log","w+")
fh.write("I love Engineering")
fh.close()

for x in os.listdir('.'):
    if x == "practicedir.log":
        logfile=open("%s"%x, "r+")
        file_content=logfile.read()
        file_content=file_content.replace('Engineering','Business')
        logfile.close()
        logfile=open("%s"%x,'w+')
        logfile.write(file_content)
        print(file_content)
        logfile.close()



with open("practicedir.log", "r+") as file:
    x=file.read()
with open("practicedir.log", "w+") as file:
    x=x.replace('Business','Engineering')
    file.write(x)
    print(x)


workdir=os.getcwd()
#print(workdir)

workdir_new=workdir.split('/')
print(workdir[0])
#print(workdir[1])

'''
