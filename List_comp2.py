#Store all special characters from the given text - "Abc@123#"
#ASCII value of Special Characters (32–47 / 58–64 / 91–96 / 123–126):
str="Abc@123#"
L=[i for i in str if 32<=ord(i)<=47 or 58<=ord(i)<=64 or 91<=ord(i)<=96 or 123<=ord(i)<=126]
print(L)
#ord() is inbuilt function use to find ascii value of characters,numbers and special characters.

