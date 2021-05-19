#3.Write a function “perfect()” that determines if parameter number is a perfect number. 
#Use this function in a program that determines and
#prints all the perfect numbers between 1 and 1000.

def perfect(n) : #perfect() user defined function
    sum=0 #initial value
    for i in range(1,n) : # start=1 stop=n-1 step=+1
        if n%i==0 : #modulus is used to find factors of n
            sum=sum+i #sum of factors
    if sum==n : #if sum factors of n equal to n then n is perfect number
        print(n)

#main program
print('Perfect numbers between 1 to 1000 ')
for i in range(1,1001) : #start=1 stop=1000 step=+1
    perfect(i) #calling user defined function
