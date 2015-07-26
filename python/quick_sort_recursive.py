'''import random

l = random.sample(range(1,500),25)
print("Original list: ",l)
print("Sorted list: ",qs_rec(l))
'''

def qs_rec(lst,start = 0, end = None):
    '''This function quick-sorts the given list from the start to end position and returns the sorted list.\nYou can specify a subset of the list for a sorted sub-list. '''
    if end is  None:
        end = len(lst)-1
    lst = lst[start:(end+1)]
    if not lst:
         return []
    else:
        lt = [x for x in lst if x < lst[0]]
        et = [x for x in lst if x == lst[0]]
        gt = [x for x in lst if x > lst[0]]
        return qs_rec(lt) + et  + qs_rec(gt)
