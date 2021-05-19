#Write a program to print number between 1 to 50 ascending in descending order
L=[i for i in range(1,51)]
L.sort(reverse=True)
print(L)
