# This program check if a number is even,
# odd, prime and palindromic
n = int(input("Write an integer number to check:\n"))

def even_odd(m):
    if n%2 == 0:
        print("The number is even \n")
    else:
        print("The number is odd \n")
        
even_odd(n)

n_string = str(n)
n_rev = n_string[::-1]

if n_string == n_rev:
    print("The number is palindromic \n")

from math import sqrt

def isPrime(j):
 
    # Corner case
    if (j <= 1):
        return False
    
    for i in range(2, int(sqrt(j))+1):
        if (j % i == 0):
            return False
    return True
 
if isPrime(n):
    print("The number is prime \n")
