import random

print("Enter an integer number.")
n = int(input("Your input: "))
a = 1
b = 1
c = 1

"""finding the nth entry in the fibonacci sequence"""
for i in range(2,n):
    a = b
    b = c
    c = a + b

print("Entry number %d in the Fibonacci sequence is the number %d" %(n,c))

"""checking if c is prime with Fermat's little theorem"""
prime = 1
for i in range(1,20):
    r = random.randint(1,c)
    check = r**c - r
    if check % c != 0:
        prime = 0
        break

if prime == 1:
    print(c, " is prime.")
else:
    print(c, " is composite.")
    
