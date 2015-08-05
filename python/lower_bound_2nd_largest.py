import math 
def sec_lar(lst):
    a, lar = 0, lst[0] 
    i = 0
    largest = lst[0]
    while i <= len(lst):
        offset = 2**a
        j = i
        while True:
            offsetted_i = i+offset
            if (offsetted_i or i) > len(lst)-1:
                break
            print(i,offsetted_i)
            if lst[i] > lst[offsetted_i]: 
                lst[i],lst[offsetted_i] = swap(lst[i],lst[offsetted_i])
                print("Swapped",i,offsetted_i,lst[i],lst[offsetted_i])
            lar = lst[offsetted_i]
            if largest > lar:
                lar = largest
            print("largest = ", lar)
            i = i + 2**(a+1)
        print("A pass completed.",lst)
        largest = lar
        a += 1
        i = j + 2**a - 1
    return lst,lar

def swap(a,b):
    return b,a
