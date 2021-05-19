#Store all the vowels from the given text - "Hello world" (Store only unique values)
str="Hello world"
print(str)
#to store vowels a,e,i,o,u
L=[ i for i in str if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' ] #list comprehension
#we want unique values only so we convert list into set
#because set stores only unique values 
a=set(L) #convert list into set and store in variable a
L=list(a) #convert set into list and store in variable L
print(L)

