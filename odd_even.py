#Use conditional statement to check is a number is even or odd.
while(True):
    a=int(input('Enter a number : '))
    if a%2==0:
        print('{} is even number'.format(a))
    else :
        print('{} is odd number'.format(a))
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break
