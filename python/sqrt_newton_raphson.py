def sqrt(n):
    x0, f, fprime, accuracy, dividend_limit = 1, lambda x,n: x**2 - n, lambda x: 2*x, 10**(-7), 10**(-14)
    max_iterations, found_ans = 50, False

    #while True
    for x in range(0,max_iterations):
        y = f(x0,n)
        yprime = fprime(x0)
        if(abs(yprime) < dividend_limit):
            print("Too small of a number to be divided.")
            break

        x1 = x0 - y/yprime

        if(abs(x1 - x0)/abs(x1) < accuracy):
            found_ans = True
            return x1

        x0 = x1

    if(found_ans == False):
        print("Answer didn't converge.")
    
        
