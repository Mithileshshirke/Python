#1.Create a Food Storage System which perform following Operation on it.
#using OOPS Concept (Class and Object )

class Food :#user defined class,base class
    def __init__(self) : #constructor
        self._d={'foodid':['1','2','3','4','5'],'foodname':['eggs','rice','roti','chicken','paneer'],'foodtype':['nonveg','veg','veg','nonveg','veg'],'foodprice':[60,80,10,150,120]}
    def __del__(self): #destructor
        pass

class FoodStorageSystem(Food) : #derived class inherits base class
    def __init__(self):#constructor
        super().__init__()
    def addfood(self):#method to add food into existing list
        while (True):
            a=input('Enter food Id : ')
            b=input('Enter food Name : ')
            c=input('Enter food Type(Veg/Nonveg): ')
            d=int(input('Enter food Price : '))
            self._d['foodid'].append(a) #append() used to add element in list
            self._d['foodname'].append(b.lower())#lower() used to conver string into lower case
            self._d['foodtype'].append(c.lower())
            self._d['foodprice'].append(d)
            ans=input('Do you want to add more (Y/N) : ')
            if ans=='N' or ans=='n':
                break
    def updatefood(self) : #method to update food
        while (True):
            a=input('Enter Food id to update food : ')
            m=self._d['foodid'].index(a)
            b=input('Enter new food Name : ')
            c=input('Enter new food Type(Veg/Nonveg): ')
            d=int(input('Enter new food Price : '))
            for i in range(len(self._d['foodid'])):
                if i==m:
                    self._d['foodname'][i]=b.lower()
                    self._d['foodtype'][i]=c.lower()
                    self._d['foodprice'][i]=d
            ans=input('Do you want to make more changes (Y/N) : ')
            if ans=='N' or ans=='n':
                break
    def deletefood(self): #method to delete food
        while(True):
            a=input('Enter Food id to delete food : ')
            m=self._d['foodid'].index(a)
            for i in range(len(self._d['foodid'])) :
                if i==m :
                    del self._d['foodid'][i]
                    del self._d['foodname'][i]
                    del self._d['foodtype'][i]
                    del self._d['foodprice'][i]
                else:
                    continue
            ans=input('Do you want to make more changes (Y/N) : ')
            if ans=='N' or ans=='n':
                break
    def show1(self): #Show Food List
        for row in zip(*([key]+(value) for key,value in self._d.items())):
            print(*row,  '  ')
    def show2(self): # Show Food using id
        a=input('Enter Food id : ')
        m=self._d['foodid'].index(a)
        for i in range(len(self._d['foodid'])):
            if i==m:
                print(self._d['foodname'][i])
                print(self._d['foodtype'][i])
                print(self._d['foodprice'][i])
    def show3(self): #Show Food using name
        a=input('Enter Food name : ')
        a=a.lower()
        m=self._d['foodname'].index(a)
        for i in range(len(self._d['foodname'])):
            if i==m:
                print(self._d['foodid'][i])
                print(self._d['foodtype'][i])
                print(self._d['foodprice'][i])
    def show4(self): #Show Foodby type
        a=input('Enter Food type : ')
        a=a.lower()
        L1=[i for i in range(len(self._d['foodtype'])) if self._d['foodtype'][i]=='veg'] #list comprehension
        L2=[i for i in range(len(self._d['foodtype'])) if self._d['foodtype'][i]=='nonveg']#list comprehension
        if a=='veg':
            for i in L1:
                print(self._d['foodid'][i])
                print(self._d['foodname'][i])
                print(self._d['foodprice'][i])
        if a=='nonveg':
            for i in L2:
                print(self._d['foodid'][i])
                print(self._d['foodname'][i])
                print(self._d['foodprice'][i])
    def sort1(self):#Sort Food List by Name
        self._d['foodname'].sort()
        print('Food name : ',self._d['foodname'])
    def sort2(self):#Sort Food List by Price
        self._d['foodprice'].sort()
        print('Food price : ',self._d['foodprice'])
    def display(self) :
        print('Food Storage System List')
        print(self._d)
    def __del__(self): #destructor
        pass
#main problem
while(True):
    obj=FoodStorageSystem() #create object of derived classs FoodStorageSystem
    obj.display() # calling method 
    while(True):
        print('\n1.Add Food\n2.Update Food\n3.Delete Food\n4.Show Food List\n5.Show Food by Id\n6.Show Food by Name\n7.Show Food by Type\n8.Sort Food List by Name\n9.Sort Food List by Price\n10.Exit')
        op=int(input('Enter your choice : '))
        if op==1:
            obj.addfood() # calling method
            obj.display()
        elif op==2:
            obj.updatefood()# calling method
            obj.display()
        elif op==3:
            obj.deletefood()# calling method
            obj.display()
        elif op==4:
            obj.show1()# calling method
        elif op==5:
            obj.show2()# calling method
        elif op==6:
            obj.show3()# calling method
        elif op==7:
            obj.show4()# calling method
        elif op==8:
            obj.sort1()# calling method
        elif op==9:
            obj.sort2()# calling method
        else:
            break
    ans=input('Do you want to continue (Y/N) : ')
    if ans=='N' or ans=='n':
        break
del obj

            
            

