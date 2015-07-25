def qs_rec(lst,start = 0, end = None):
    if end is None:
        end = len(lst)-1
    lst = lst[start:(end+1)]
    print(lst)
    if not lst:
        return []
    else:
        lt = [x for x in lst if x < lst[0]]
        et = [x for x in lst if x == lst[0]]
        gt = [x for x in lst if x > lst[0]]
        return qs_rec(lt) + et  + qs_rec(gt)
