from randomized_quick_sort import partition_f

def kthsmallest(lst, k, f = 0, l = None):
    if l is None:
        l = len(lst) - 1
    k_counter = 0
    while True:
        pos = partition_f(lst,f,l)
        length = pos - f + 1
        if k == length:
            return lst[pos]
        elif k < length:
            l = pos - 1
        else:
            k = k - length
            f = pos + 1
        

