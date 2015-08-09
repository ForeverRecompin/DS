from random import choice
def qs(lst, f = 0,l = None):
    if l is None:
        l = len(lst) - 1
    if f < l:
        partition = partition_f(lst,f,l)
        qs(lst,f,partition-1)
        qs(lst,partition+1,l)
    return lst

def partition_f(lst,f,l):
    p_index = choice(range(f,l))
    lst[p_index], lst[f] = lst[f], lst[p_index]
    pivot = lst[f]
    lo, hi = f, l
    while lo < hi:
        while lst[lo] <= pivot and lo < l:
            lo += 1
        while lst[hi] > pivot:
            hi -= 1
        if lo < hi:
            lst[lo], lst[hi] = lst[hi], lst[lo]
    lst[hi], lst[f] = lst[f], lst[hi]
    return hi
