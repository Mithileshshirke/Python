#3. Write a Program in python to Explain all type of inheritance
#here class Details and class marks inherites class Students
#class Attendance inherites class Students and Teacher
#class Marks inherites class Students and class Result inherits class Marks
class Students : #base class 1
    def __init__(self) : #constructor
        self.__name=input('Enter Student Name : ')
        self.__rno=int(input('Enter Roll Number : '))
    def display(self) : #method 
        print('Name : ',self.__name)
        print('Roll Number : ',self.__rno)
    def __del__(self) : #destructor
        pass
class Teacher : #base class 2
    def __init__(self) :
        self._lect=int(input('Number of lectures held by teachers : '))
    def __del__(self) : #destructor
        pass
class Attendance(Students,Teacher) : #derived class inherits base class1 and base class2
    def __init__(self) : #constructor
        super().__init__()#calling constructor of base class 1
        Teacher.__init__(self)#calling constructor of base class 2
        self._attend=int(input('Number of lectures attend by student : '))
    def display(self) :
        self._per=round(self._attend*100/self._lect)
        print()
        print('Percentage of attendance : {}%'.format(self._per))
        if self._per>=75:
            print('Allow to sit for exam')
        else:
            print('Not allowed to sit for exam')
    def __del__(self) : #destructor
        pass

#main program example of multiple inheritance
allow=Attendance() #create object of derived class Attendance
allow.display() #calling display method
del allow
class Details(Students) : #derived class inherits base class1 Student
    def __init__(self) :
        super().__init__() #calling constructor of base class Students
        self.__add=input('Enter Address : ')
        self.__city=input('Enter City : ')
        self.__cont=input('Enter contact number : ')
    def display(self) : #method
        print()
        super().display()#calling method of base class Students
        print('Address :{}\nCity : {}\nContact : {}'.format(self.__add,self.__city,self.__cont))
    def __del__(self) : #destructor
        pass

#main program example of simple and hierarchical inheritance
#as class Student has two derived class Details and Attendance
print()
det=Details() #create object of derived class Details
det.display()#calling display method
del det

class Marks(Students) : #derived class inherits base class Student
    def __init__(self) : #constructor
        super().__init__() #calling constructor of base class Students
        self._phy=int(input('Enter marks of Physics : '))
        self._chem=int(input('Enter marks of Chemistry : '))
        self._mat=int(input('Enter marks of Mathematics : '))
        self._bio=int(input('Enter marks of Biology : '))
    def display(self) : #method
        super().display()#calling method of base class Students
        print('Marks of Subjects')
        print(' Physics : {}\nChemistry : {}\nMathematics : {}\nBiology : {}'.format(self._phy,self._chem,self._mat,self._bio))
    def __del__(self) :#destructor
        pass
class Result(Marks) :#derived class inherits base class Marks
    def __init__(self) : #constructor
        super().__init__() #calling constructor of base class
    def display(self) : #method
        print()
        super().display() #calling method of base class Students
        if self._phy<40 or self._chem<40 or self._mat<40 or self._bio<40 :
            print('Result : Fail')
        else:
            _t=self._phy+self._chem+self._mat+self._bio
            _p=round(_t*100/400,2)
            print('Percentage : {}%'.format(_p))
            print('Result : Pass')
    def __del__(self) :#destructor
        pass
#main program example of multilevel inheritance
print()
res=Result() #create object of derived class Result
res.display() #calling display method
del res




