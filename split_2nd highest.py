#4) write a program to get second heighest value from the list
#list comprehension multiple input using inbuilt function split()
L=[int(x) for x in input('Enter numbers separated by space : ').split()]
#multiple input using inbuilt method split() 
print(L) 
max=0 #initial value
for i in L :
    if i>max : #condition checked
        max=i
max2=0 #initial value
for i in L :
    if max2 < i < max : #condition checked
        max2=i
print('Second heighest value from the list is ',max2)
