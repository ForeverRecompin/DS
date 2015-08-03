def largest_bitonic(lst):
    f, l = 0, len(lst) - 1
    while f <= l:
        m = f + int((l-f)/2)
        if m-1 >= 0 and m+1 <len(lst): #In between
            if lst[m] > lst[m-1] and lst[m] > lst[m+1]:
                return m,lst[m]
            elif lst[m-1] > lst[m]:
                l = m - 1
            else:
                f = m + 1
        elif m-1 >= 0: #Extreme right
            if lst[m] > lst[m] - 1:
                f = m
            else:
                l = m - 1
        else: #Extreme left
            if lst[m] > lst[m+1]:
                l = m
            else:
                f = m + 1
                
            
