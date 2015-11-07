def coins_in_a_line(pots, left, right, player):  # Using a backtrack.
    if left > right:
        return 0
    if player == 'A':
        result = max(pots[left] + coins_in_a_line(pots, left + 1, right, 'B'),
                     pots[right] + coins_in_a_line(pots, left, right - 1, 'B'))
    else:
        result = min(coins_in_a_line(pots, left + 1, right, 'A'), coins_in_a_line(pots, left, right - 1, 'A'))
    return result


def coins_dp(pots, left, right, player):  # Dynamic programming.
    from math import inf
    n = len(pots)
    default_val = float(inf)
    T = [[default_val for _ in range(n)] for _ in range(n)]

    def memoized_soln(left, right, player):
        nonlocal T, pots
        if left > right:
            return 0
        if T[left][right] != default_val:
            return T[left][right]
        if player == 'A':
            result = max(pots[left] + memoized_soln(left + 1, right, 'B'),
                         pots[right] + memoized_soln(left, right - 1, 'B'))
        else:
            result = min(memoized_soln(left + 1, right, 'A'), memoized_soln(left, right - 1, 'A'))
        T[left][right] = result
        return result

    return (memoized_soln(left, right, player))


def main():
    pots = [3, 1, 9, 2]
    left, right = 0, len(pots) - 1
    result = coins_in_a_line(pots, left, right, 'A')
    print("A's value: ", result)
    result = coins_dp(pots, left, right, 'A')
    print("A's value by using DP: ", result)


if __name__ == "__main__":
    main()
