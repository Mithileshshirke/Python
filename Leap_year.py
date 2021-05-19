#Use conditional statement to check if a year is a leap year or not.
while(True) :
    y=int(input('Enter Year : '))
    if y%4==0:#condition check for number is divisible by 4 or not
        if y%100!=0:#nested if else i.e. inner if
            print('{} is Leap year'.format(y))
        elif y%400==0:#else of inner if
            print('{} is Leap year'.format(y))
        else :#else of inner if
            print('{} is not a Leap year'.format(y))
    else:#outer else
        print('{} is not a Leap year'.format(y))
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break

