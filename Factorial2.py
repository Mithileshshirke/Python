#WAP to find factorial of number.(4!=4*3*2*1)
n=int(input('Enter number : '))
m=1#initial value for multiplication
if n==0:
    print('Factorial of zero is 1')
else:
    for i in range(1,n+1) :
        m=m*i #for factorial multiplication
    print('factorial of {} is {} '.format(n,m))
input()
