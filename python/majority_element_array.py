def majority_element(lst):
    if len(lst)  > 1:
        mid = int(len(lst)/2)
        left = lst[:mid]
        right = lst[mid:]
        left, nl, fl = majority_element(left)
        #print(left, nl, fl,"LEFT")
        right, nr, fr = majority_element(right)
        #print(right, nr, fr,"RIGHT")
        sorted_lst, ns, fs = merge(left,right,nl,fl,nr,fr)
        #print( sorted_lst, ns, fs,"COMMON")
        #print("MAJORITY L",nl," R,",nr,"COUNT L",fl," R ",fr)
        if len(sorted_lst)//2 < fs:
            return sorted_lst,ns,fs
        else:
            if fl > fr:
                return sorted_lst,nl,fl
            else:
                return sorted_lst,nr,fr
    else:
        return lst,0,0

def maj_element(lst):
    _,element,_ = majority_element(lst)
    count = 0
    for each in lst:
        if each == element:
            count += 1

    return element,count

def merge(l,r,nl,fl, nr, fr):
    #print("TESTINGGGGGGG",l,r)
    #print("MAJORITY L",nl," R,",nr,"COUNT L",fl," R ",fr)
    if nl == nr:
        majority = nl
        count = fl + fr
    elif fl > fr:
        majority = nl
        count = fl
    else:
        majority = nr
        count = fr
        
    aux_lst = []
    i, j,  = 0, 0

    if (len(l) + len(r)) == 2:
        if l[0] == r[0]:
            majority = l[0]
            count += 2

    elif count == fl: # Look for majority elements in right
        for each in r:
            if each == majority:
                count += 1
    else: #Look into left list
        for each in l:
            if each == majority:
                count += 1
    
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
    return aux_lst,majority,count
