#WAP to find factorial of number.
while(True):
    n=int(input('Enter number : '))
    i=1#initial value
    m=1#initial value for multiplication
    if n==0:
        print('Factorial of zero is 1')
    else:
        while i<=n :
            m=m*i #for factorial multiplication
            i=i+1
        print('factorial of {} is {} '.format(n,m))
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break
