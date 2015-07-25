def qs_rec(lst):
    if not lst:
        return []
    else:
        return qs_rec([x for x in lst if x < lst[0]]) + [x for x in lst if x == lst[0]] + qs_rec([x for x in lst if x > lst[0]])
