def ps(n):
    f, l = 1, n/2
    while (f <= l):
        m = (f + (l-f)/2)
        print("m = ",m)
        if n == int(m*m):
            print(m,"\t True")
            break
        elif n > int(m*m):
            f = m + 0.001
        else:
            l = m - 0.001
