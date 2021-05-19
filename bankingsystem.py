#2) write a program to make banking system develop business logic
#in one module and call functionality in another .py file

class Customer: #user defined class
    def __init__(self,name,phoneno,address,pin,accno,balance) : #constructor with multiple arguments
        self._name=name 
        self._pno=phoneno
        self._add=address
        self._pin=pin
        self._acc=accno
        self._bal=balance#protected variable
    def add(self) : #user defined method
        self._d={} #create empty dictionary
        self._d['CustomerName']=self._name #add values to the dictionary using key names
        self._d['CustomerPhonenumber']=self._pno
        self._d['CustomerAddress']=self._add
        self._d['CustomerPin']=self._pin
        self._d['CustomerAccountNumber']=self._acc
        self._d['CustomerBalance']=self._bal
        print('Customer Details Add Successfully')
    def deposit(self):
        amt=int(input('Enter Deposit amount : '))
        self._d['CustomerBalance']+=amt
        print('Your a/c is credited for INR ',amt)
        print('Account Balance is ',self._d['CustomerBalance'])
        print()
    def withdraw(self):
        amt=int(input('Enter Withdraw amount : '))
        if amt>self._d['CustomerBalance'] :
            print('Insufficient Balance')
            print('Account Balance is ',self._d['CustomerBalance'])
            print()
        else:
            self._d['CustomerBalance']-=amt
            print('Your a/c is debited for INR ',amt)
            print('Account Balance is ',self._d['CustomerBalance'])
            print()
    def transfer(self):
        name=input('Enter Recipient name : ')
        acc=input('Enter account number : ')
        if len(acc)==16:
            amt=int(input('Enter amount to transfer : '))
            if amt>self._d['CustomerBalance'] :
                print('Insufficient Balance')
                print('Account Balance is ',self._d['CustomerBalance'])
                print()
            else:
                self._d['CustomerBalance']-=amt
                print('Transfer amount successfully')
                print('Your a/c is debited for INR ',amt)
                print('Account Balance is ',self._d['CustomerBalance'])
                print()
        else:
            print('Invalid Account Number\n')
    def mini(self):
        print('Name : ',self._d['CustomerName'])
        print('Account Balance is ',self._d['CustomerBalance'])
        print()
    def __del__(self): #destructor
        print('Thank You')
        pass

