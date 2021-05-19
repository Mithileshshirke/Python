'''write a program to check user entered number is perfect or not 
n=6 
1+2+3 all diviser sum is also 6 so 6 is perfect number '''

n=int(input('Enter number : '))
sum=0 #initial sum
print( 'Factors of {} are '.format(n))
for i in range(1,n) :  #start=1,stop=n-1,step=+1
    if n%i==0 : #to find remainder value to check n is divisible by which number
        print(i) 
        sum=sum+i  #sum of numbers that divides n i.e. addition of factors of n
print('Sum : ',sum)
if sum==n :  #condition checked
    print('{} is a Perfect number'.format(n))
else:
    print('{} is not a Perfect number'.format(n))
input()
