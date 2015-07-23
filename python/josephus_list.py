def josephus(lst_capacity,pos_to_kill):
    '''Returns the sequence of prisoners killed and the survivor-prisoner.'''
    lst, index, seq_killed  = list(range(lst_capacity)), 0, [] #Index positions start from 0.
    while lst:
        index = (index + pos_to_kill - 1) % len(lst)
        person_killed = lst.pop(index)
        seq_killed.append(person_killed)
    return (seq_killed[:-1],seq_killed[-1])
