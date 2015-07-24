def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if (lst[j+1] <  lst[j]):
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst
