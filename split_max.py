#1) write a program to find maximum number from the list
#without using function and slicing or sorting funtion
L=[float(i) for i in input('Enter numbers separated by space : ').split() ]
#multiple input stored in list using inbuilt function split()
print(L)
max=0 #initial value
for i in L : 
    if i > max : #condition to check max number
        max=i
print('Maximum number from list is ',max)
 
