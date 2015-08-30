def knap01(in_weight, lst_weight_val):
    ''' in_weight = Knapsack size,
        lst_weight_val = list of weight-value tuples.
        Function returns Max value and weight-items chosen'''
    wt = [each[0] for each in lst_weight_val]
    val = [each[1] for each in lst_weight_val]
    t = [[0 for _ in range(in_weight + 1)] for _ in range(len(val))]
    for i in range(len(val)):
        for j in range(1,in_weight +1):
            if wt[i] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = max(t[i-1][j], val[i] + t[i-1][j-wt[i]])
    '''i, j, items = len(val) - 1, in_weight, []
    while i != 0 and j != 0:
        if t[i][j] != t[i-1][j]: #ith item was taken
            items.append(wt[i])
            j = j - val[i]
            i = i - 1
        else:  #ith item wasn't taken
            items.append(wt[i-1])
            j = j - val[i-1]
            i = i - 1 -1'''
            
    return t[len(val) - 1][in_weight] #, items.reverse()

