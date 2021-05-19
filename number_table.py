#write a program to display multiplication table for given number
n=int(input('Enter number : '))
for i in range(1,11) :
    print('{}*{}={}'.format(n,i,n*i))
