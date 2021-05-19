''' A company decided to give bonus of 5% to employee if his/her year of service is more than
5years.
ask user for their salary and year of service and print net bonus.'''
while(True):
    s=int(input('Salary(monthly) : '))
    y=int(input('Year of service : '))
    if y>5 :
        b=s*0.05
        S=s+b
        print('Bonus is ',b)
        print('Net bonus amount is ',S)
    else:
        print('Bonus is applicable to employee whose year of service is more than 5years')
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break

