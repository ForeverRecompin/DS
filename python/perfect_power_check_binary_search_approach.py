import math

def per_pow(n):
    f, l = 2, n
    while(f <= l):
        m = f + int((l-f)/2)
        if n == m ** int(math.log(n,m)):
            return True
        elif n < m ** int(math.log(n,m)):
            l = m - 1
        else:
            f = m + 1
    return False
