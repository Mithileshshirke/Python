# Store all numbers divisible by 5 from the given dictionary
d={"a":15,"b":20,"c":31,"d":46,"e":65}#given dictionary
L=[i for i in d.values() if i%5==0 ] #list comprehension
#values() is inbuilt method use to access all values of keys.
#condition check if number is divisible by 5 we use % to find remainder value
print(L)
