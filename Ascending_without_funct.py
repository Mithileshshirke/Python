#5) write a program to sort integer and character based list into ascending order 
#without using functions

L=['12','45','mits','55','abcd','7','big']
d=[]#create empty list
s=[]#create empty list
for i in L :
    if i.isdigit() : #to check given value is digit or charcter
        d.append(int(i)) #inbuilt method append() use to add elements in list
    else:
        s.append(i)#inbuilt method append() use to add elements in list
print(d,'\n',s)

#ascending order integers without using functions
for i in range(0,len(d)) : #start=0 stop=n-1 step=+1
    for j in range(i+1,len(d)) :#start=i+1 stop=n-1 step=+1
        if d[i]>d[j]: 
            d[i],d[j]=d[j],d[i] #swapping
print('Ascending order integers\n',d)

#ascending order characters without using functions
for i in range(0,len(s)) :#start=0 stop=n-1 step=+1
    for j in range(i+1,len(s)) : #start=i+1 stop=n-1 step=+1
        if s[i]>s[j]:
            s[i],s[j]=s[j],s[i] #swapping
print('Ascending order characters\n',s)
