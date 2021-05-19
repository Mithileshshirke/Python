#write a function to find prime factor  of given number
#passing argument but no return value
def primefact(a) : #user defined function
    print('Prime factors of {}'.format(a))
    for i in range(2,a+1): #start=2 stop=a step=+1 #we ignore 1 because it is not prime
        if a%i==0: #remainder is used to find factors of a
            for j in range(2,i): #start=2 stop=i-1 step=+1
                if i%j==0  : #remainder is used to check whether factors are prime or not
                    break #to exit from loop directly
            else:
                print(i)

#main program
n=int(input('Enter number : '))
primefact(n)#calling user defined function
