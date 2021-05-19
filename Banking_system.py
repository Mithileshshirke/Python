import bankingsystem as B
n=input('Enter Customer name : ')
while(True):
    try : #try block contains code which may cause exception
        pno=input('Enter Phone number : ')
        assert pno.isdigit(),'Please enter 10 digit phone number'
        assert len(pno)==10,'Please enter 10 digit phone number'
        break
    except AssertionError as a: #catch exception raise in try block,here AssertionError is inbuilt exception
        print(a)
add=input('Enter Address : ')
while(True):
    try:
        pin=input('Enter Pin : ')
        assert len(pin)==6,'Please Enter 6 Digit Pin'
        break
    except AssertionError as a: #catch exception raise in try block,here AssertionError is inbuilt exception
        print(a)
while(True):
    try:#try block contains code which may cause exception
        acc=input('Enter account number : ')
        assert acc.isdigit(),'Please enter 16 digit account number'
        assert len(acc)==16,'Please enter 16 digit account number'
        break
    except AssertionError as a: #catch exception raise in try block,here AssertionError is inbuilt exception
        print(a)
bal=int(input('Enter balance : '))
cust=B.Customer(n,pno,add,pin,acc,bal) #create object from class Customer
cust.add() #calling add method of class using object
while(True): #outer loop
    x=input('Do you want to start banking (Y/N) : ')
    if x=='N' or x=='n':
        break #exit directly from outer loop
    else:
        c=0 #initial count
        while(True):#inner loop1/nested while loop
            ac=input('Enter account number : ')
            pinn=input('Enter pin : ')
            c=c+1
            if ac==acc and pinn==pin:
                while(True):#inner loop2 /nested while loop
                    print('1.Deposit\n2.Withdraw\n3.Transfer\n4.Mini Statement\n5.Quit')
                    ch=input('Enter your choice : ')
                    print()
                    if ch=='1':
                        cust.deposit()
                    elif ch=='2':
                        cust.withdraw()
                    elif ch=='3':
                        cust.transfer()
                    elif ch=='4':
                        cust.mini()
                    else:
                        break #exit from inner loop 2
                break #exit from inner loop 1
            else:
                print('Invalid a/c number or pin')
                if c==3:
                    print('You have exceed number of chances,Try after some time')
                    break#exit from inner loop 1
        break #exit from outer loop
del cust                 
