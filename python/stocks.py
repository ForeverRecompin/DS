def stocks_finder(lst):
    '''Returns a tuple (a,b,c,d):
       a: Minimum buying price
       b: Day of " " " 
       c: Maximum selling price
       d: Day of " " " 
    '''
    buy,sell = merge_sort(lst)
    return buy,lst.index(buy),sell,lst.index(sell)

def merge_sort(lst, b = 0, s = 0):

    if len(lst) > 1:
        mid = int(len(lst)/2)
        left = lst[:mid]
        right = lst[mid:]
        bl,sl = merge_sort(left)
        br,sr = merge_sort(right)
        b,s = merge(left,right)
        profit_l, profit_r, profit_lr = sl - bl, sr - br, s - b
        max_profit = max(profit_l,profit_r,profit_lr)
        if max_profit == profit_l:
            return bl,sl
        elif max_profit == profit_r:
            return br,sr
        else:
            return b,s 
    else:
        return 0,0

def merge(l,r):
    aux_lst = []
    i, j,  = 0, 0
    buy, sell = l[0], r[0]
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            #aux_lst.append(l[i])
            if buy > l[i]:
                buy = l[i]
            i += 1
        else:
            if sell < r[j]:
                sell = r[j]
            #aux_lst.append(r[j])
            j += 1
            
    while i < len(l):
        #aux_lst.append(l[i])
        if buy > l[i]:
                buy = l[i]
        i += 1
    while j < len(r):
        #aux_lst.append(r[j])
        if sell < r[j]:
                sell = r[j]
        j += 1
    aux_lst = l + r
    return buy,sell
