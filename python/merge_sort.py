def merge_sort(lst):
    if len(lst) > 1:
        mid = int(len(lst)/2)
        left = lst[:mid]
        right = lst[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        sorted_lst = merge(left,right)
        return sorted_lst
    else:
        return lst

def merge(l,r):
    aux_lst = []
    i, j,  = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            aux_lst.append(l[i])
            i += 1
        else:
            aux_lst.append(r[j])
            j += 1
            
    if i < len(l):
        aux_lst += l[i:]
    if j < len(r):
        aux_lst += r[j:]
    return aux_lst
