def bs(lst,key,beg = 0,end = None):
    lst.sort()
    if end is None:
        end = len(lst) - 1
    if beg > end:
        return False
    else:
        mid = int (beg + (end-beg)/2)
        if key == lst[mid]:
            return (True,mid)
        elif key < lst[mid]:
            end = mid - 1
            return bs(lst,key,beg,end)
        elif key > lst[mid]:
            beg = mid + 1
            return bs(lst,key,beg,end)
            
