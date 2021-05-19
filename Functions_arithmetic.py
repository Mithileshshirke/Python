#1) Create functions for addition, subtraction, multiplication, division, square root 
#addition
def addition(x,y) : #user defined function
    return x+y
#main program
a=float(input('Enter first number : '))
b=float(input('Enter second number : '))
print('Addition is ',addition(a,b)) #calling user defined function
#give sum of all values in list

#########################################################
#subtraction
def subtraction(x,y) :#user defined function
    return x-y
#main program
a=float(input('Enter first number : '))
b=float(input('Enter second number : '))
print('Subtraction is ',subtraction(a,b))#calling user defined function
#give sum of all values in list

############################################################
#multiplication 1
def multiplication(x,y) : #user defined function
    return x*y
#main program
a=float(input('Enter first number : '))
b=float(input('Enter second number : '))
print('Multiplication is ',multiplication(a,b))#calling user defined function
#give multiplication of all values in list

###################################################################
#division
def division(x,y):#user defined function
    return x/y
#main program
a=float(input('Enter first number : '))
b=float(input('Enter second number : '))
print('Division is ',division(a,b))#calling user defined function
#give division of all values in list

##################################################################
#square root
from math import sqrt
def sqr(a):#user defined function
    return sqrt(a)
#main program
a=float(input('Enter number : '))
print('Square root is ',sqr(a))#calling user defined function
#give square root of all values in list
