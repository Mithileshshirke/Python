#WAP to calculate BMI
while(True):
    h=float(input('Height(cm) = '))
    w=float(input('Weight(kg) = '))
    b=w/(h/100)**2#here b is for bmi & 1meter=100cm
    if b<18.5:#condition checked
        print('Underweight')
    elif 18.5<=b<=24.9:#multiple if else
        print('Normal weight')
    elif 25<=b<=29.9:
        print('Overweight')
    else :
        print('Obesity')
    a=input('Do you want to continue (Y/N) : ')
    if a=='n' or a=='N':
        break

