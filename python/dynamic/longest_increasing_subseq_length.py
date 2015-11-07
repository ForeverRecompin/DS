def longest_inc_subseq(lst):
    """
    Args:
        A list of numbers whose length of longest
        increasing subsequence has to be found
    Returns:
        length of longest increasing subsequence
    """
    n = len(lst)
    lst_copy = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if lst[i] > lst[j] and lst_copy[i] < lst_copy[j] + 1:
                lst_copy[i] = lst_copy[j] + 1

    return (max(lst_copy))


def main():
    lst = [10, 22, 9, 33, 21, 50, 41, 60]
    print(longest_inc_subseq(lst))
    assert longest_inc_subseq(lst) == 5, "Meh, this doesn't work! :/"


if __name__ == "__main__":
    main()
