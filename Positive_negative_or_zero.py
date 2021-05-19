#Python program to check if number is positive,negative or zero.
while(True):
    n=float(input('Enter a number : '))
    if n> 0:#condition check
        print('Given number is Positive')
    elif n==0:#multiple if else
        print('Given number is Zero')
    else :
        print('Given number is Negative')
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break
    


