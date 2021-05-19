#Store the square root of all the even numbers between 1 to 20.
from math import sqrt #import function to find square root from math library 
L=[round(sqrt(i),2) for i in range(1,21) if i%2==0] #list comprehension
#round() is inbuilt function use to round values 2digits after decimal point
#modulus is used in condition is find remainder if remainder is 0 then it is even number
print(L)
