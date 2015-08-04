def josephus(n = 41,k = 3):
    '''Returns the position of the survivor.\nInputs: n = number of participants, k = kth person is killed.\neg: josephus(41,3) = 31'''  
    if n == 1:
        return 1
    else:
        return (josephus(n-1,k)+k-1)%n+1
