import math
from fractions import gcd
from functools import reduce

def prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
                   
def per_pow(n):
    ''' Checks if a number n is a perfect power number.\nA perfect power number if one which can be expressed as a**b, where a,b > 1'''
    count_2 = 0
    divisors = dict()
    while (n%2==0):
        n = int(n/2)
        count_2 += 1
    if count_2 != 0:
        divisors[2] = count_2
    for i in range(3,n+1,2):
        count = 0
        while(n%i==0):
            n = int(n/i)
            count += 1
        if count != 0:
            divisors[i] = count
    potential_prime_divisors = list(divisors.keys())
    prime_divisors = []
    for i in range(0,len(divisors)):
        if prime(potential_prime_divisors[i]):
            prime_divisors.append(potential_prime_divisors[i])
    return (reduce(gcd,prime_divisors) > 1)
