def merge_sort(lst, inversions = 0):
    if len(lst)>1:
        mid = int(len(lst)/2)
        left = lst[:mid]
        right = lst[mid:]
        left,inv_l = merge_sort(left)
        #print(left,inv_l)
        right,inv_r = merge_sort(right)
        #print(right,inv_r)
        merged,inv_lr = merge(left,right)
        #print(merged,inv_lr)
        return merged,(inv_l+inv_r+inv_lr)
    else:
        return lst,0

def merge(left,right):
    aux_lst = []
    i, j = 0, 0
    inversion_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            aux_lst.append(left[i])
            i += 1
        else:
            aux_lst.append(right[j])
            inversion_count += len(left) - (i) 
            j +=1 

    while i < len(left):
            aux_lst.append(left[i])
            i  += 1
    while j < len(right):
            aux_lst.append(right[j])
            j +=1

    return aux_lst,inversion_count
