'''write a program to check user-entered number is palindrome or not
n=121 rev=121 n=rev'''


n=int(input('Enter number : '))
x=n
rev=0
while x>0 :
    y=x%10
    rev=rev*10 + y
    x=x//10
print('Reverse = ',rev)
if n==rev :
    print('{} is a palindrome '.format(n))
else:
    print('{} is not a palindrome '.format(n))
