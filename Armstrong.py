#Python Program to Check Armstrong Number
while(True):
    n=int(input('Enter a number : '))
    x=y=n
    c=0#count
    while x>0:#condition checked
        x=x//10 # // gives integer division
        c=c+1
    sum=0 #initial sum
    while y>0:#condition checked
        a=y%10 #gives remainder value
        sum=sum+a**3
        y=y//10 # // gives integer division
    if sum==n :
        print('{} is a Armstrong Number'.format(n))
    else :
        print('{} is not a Armstrong Number'.format(n))
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break
