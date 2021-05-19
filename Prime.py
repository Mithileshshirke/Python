#write a program to check user entered number is prime or not
n=int(input('Enter number : '))
if n>1 : 
    for i in range(2,n): #start=2 , stop=n-1,step=+1
        if n%i==0 : # condition check whether n is divisible by any other number except n.
            print('{} is not a prime number'.format(n))
            break #exit from loop
    else : 
        print('{} is a prime number'.format(n)) 
else : #condition for n is equal to 1 or less than 1 
    print('{} is not a prime number'.format(n))
