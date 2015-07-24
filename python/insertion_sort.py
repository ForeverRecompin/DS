def insertion_sort(lst):
    for i in range(1,len(lst)):
        key, j = lst[i], i-1
        while lst[j] > key and j>=0:
            lst[j+1] = lst[j]
            j = j - 1
            print(lst[j+1],j)
        lst[j+1] = key
    return lst
