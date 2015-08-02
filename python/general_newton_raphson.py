def func(exp,coefficients,x):
    ans, index = 0, 0
    while(exp != 0):
        ans = ans + coefficients[index] * x**(exp)
        exp -= 1
        index += 1
    return ans + coefficients[index]

def funcprime(exp,coefficients,x):
    ans, index = 0,0
    while(exp != 0):
        ans = ans + coefficients[index] * exp * x**(exp-1)
        exp -= 1
        index += 1
    return ans 

def solve_eq():
    '''Solves an equation with the newton-raphson method.\nInput coefficient values should be of the form x^n, x^n-1.....,x^3,x^2,x^1,+/- constant.'''
    max_pow = int(input("Enter maximum power: "))
    print("Enter coefficients.")
    coefficients = list(map(int,input().split()))
    f = lambda x: func(max_pow, coefficients,x)
    fprime = lambda x: funcprime(max_pow,coefficients,x)
    x0 = coefficients[(len(coefficients) - 1)]/2
    accuracy, dividend_limit = 10**(-7), 10**(-14)
    flag, max_iterations = False, 20

    for i in range(0,max_iterations):
        y = f(x0)
        yprime = fprime(x0)

        if abs(yprime) < dividend_limit:
            break

        x1 = x0 - y/yprime

        if abs(x1) == 0:
            break

        if abs(x1-x0)/abs(x1) < accuracy:
            flag = True
            return x1

        x0 = x1

    if(flag is False):
        print("Answer doesn't converge for the given number of max-iterations.")
        
