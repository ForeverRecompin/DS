def soe(n):
    '''
    Strike the Twos and strike the Threes,
    The Sieve of Eratosthenes!
    When the multiples sublime,
    The numbers that are left, are prime.

    Returns a list of primes <= n. 
    '''
    sieve, primes = [True] * (n+1), []
    sieve[1] = False
    i = 2
    while i*i <= n:
        if sieve[i]:
            primes.append(i)
            for j in range(i*i,n+1,i):
                sieve[j] = False
        i += 1
    for i in range(i, n+1):
        if(sieve[i]):
            primes.append(i)
    return primes

def dumb_soe(n):
    sieve, primes = [True] * (n+1), []
    for i in range(2,n+1):
        if sieve[i]: 
            primes.append(i)
            for j in range(i+i,n+1,i):
                sieve[j] = False    
    return primes
    
