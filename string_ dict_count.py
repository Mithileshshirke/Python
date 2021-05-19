'''Given string
mystr = "Hello world"
Output -
{"H":1,"e":1,"l":3,"o":2,"w":1,"r":1,"d":1}'''

mystr = "Hello world"
d={} #define empty dictionary
for i in mystr : 
    d[i]=mystr.count(i) #adding keys and values to the dictionary
#count() is inbuilt method to count of repeating characters in given string
    if i==' ' : #condition check for space 
        d.pop(' ') #pop() is inbuilt method in dictionary it delete particular key using key name
print('Given string is\nmystr=',mystr)
print('Output - ',d)
