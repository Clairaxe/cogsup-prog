"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    return n%d == 0

def is_prime(n):
    for i in range (2,n):
        if is_factor(i,n) :
            return False
    return True 


def list_prime ():
    lst=[]
    for i in range (2,10000) :
        if is_prime(i):
            lst.append(i)
    return lst

list_of_primes = list_prime()
print(list_of_primes)