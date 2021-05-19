'''Given string
mystr = "Hello world"
Ouput -
{"vowels":["e","o"], "consonants":["H","l","w","r","d"]}'''

mystr = "Hello world" #given string
mystr.lower() #lower() is inbuilt method use to conver string into lower case letters
d={} #define empty dictionary
v=[] #define empty list
c=[] #define empty list
for i in mystr : #for loop is used to access every element in string
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' : #condition check fot vowels
        if i not in v :  #condition check to avoid duplicate values
            v.append(i) #append() is inbuilt method to add element in list at last index position
    else :
        if i not in c  :  #condition check to avoid duplicate values
            c.append(i) #append() is inbuilt method to add element in list at last index position
        if i==' ' :
            c.remove(i) #remove() is inbuilt method to remove particular value in list
d["vowels"]=v #add vowels to dictionary
d["consonants"]=c #add consonants to dictionary
print('given string is \n mystr = ',mystr)
print('Output -\n',d)
