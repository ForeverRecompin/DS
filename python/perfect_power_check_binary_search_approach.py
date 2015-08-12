import math

def per_pow(n):
        ind = (math.log(n,2))
        for i in range(2,int (ind)):
            first, last = 2, n
            while(first <= last):
                mid = first + int((last - first)/2)
                print(first,"\t",last,"\t",i,"\t",mid,"\t",n)
                if n == mid ** i:
                    return True
                elif n > mid ** i:
                    first = mid + 1
                elif first == last:
                    if n == first ** i:
                        return True
                else:
                    last = mid - 1
        return False
