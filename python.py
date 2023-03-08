#!/usr/bin/python

#Variable Declaration
x =5
y ="I love python"
z="I love being a cloud engineer"
p,q,s=10,15,20


#Main body
print(x)
print(y)
print (x, y)

#using + sign
print("I love the number " + str(x) )
print("x is variable " + str(x) + " is the value" )

#using .format
#This is how to add variable to a string using the format function
print("The value of y is: {}, and the value of z is: {}, and the value of x is: {}".format(y,z,x) )
print("The value of x is: {}".format(x) )
print("The value of z is: {}".format(z) )
print("The value of p is: {}, the value of q is: {}, the value of s is: {}".format(p,q,s) )
print ("p is the variable and {} is the value, s is the variable and {} is the value, s is the variable and {} is the value".format(p,q,s) )
print("{} {} {}".format(x,y,z) )

#Using comma
print('x is the variable,',x,' is the value')

#using % sign
print("x is the variable, %s is the value"%x)


