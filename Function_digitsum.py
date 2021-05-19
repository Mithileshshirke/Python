#Write a function to display sum of digits of given number
def digitsum(a) : #digitsum() is user defined function
    s=0 #initial sum value
    while a>0: #condition check
        y=a%10 # modulus is use to add individual digit
        s=s+y #increment
        a=a//10 #integer division
    return s #return value where function is called

#main
n=int(input('Enter number : '))
print('Sum of digits of number {} is {}'.format(n,digitsum(n))) #calling user defined function
