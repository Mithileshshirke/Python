#2) mylist = [11,14,5,78,45,67,9,88,10]
#a) apply filter to create a list of palindrome numbers from mylist
def rev(n): #user defined function
    r=0
    while n>0:
        y=n%10 #to find remainder value
        r=r*10+y #rev increment
        n=n//10 #integer division
    return r
#main
mylist = [11,14,5,78,45,67,9,88,10]
L=list(filter(lambda a : a==rev(a) ,mylist))#condition check for reverse is equal to number
print('List of palindrome numbers\n',L)


#b) apply filter to create a list of numbers divisible  by 3 or 5 from the mylist
mylist = [11,14,5,78,45,67,9,88,10]
d=list(filter(lambda a : a%3==0 or a%5==0 ,mylist))
print('List of numbers divisible  by 3 or 5\n',d)
