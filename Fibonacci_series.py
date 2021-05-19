'''write a program to print fibonacci serise 
 0,1,1,2,3,5,8 till user entered number'''
n=int(input('Fibonacci series till entered number: '))
n1=0 #initial values of  fabonacci series
n2=1  #initial values of  fabonacci series
print(n1)
print(n2)
for i in range(n-2): #start=0 stop=n-2-1=n-3 step=+1
    a=n1+n2
    print(a)
    n1=n2 #assigning value of n2 to n1
    n2=a #assigning value of a to n2
input()
    

    
