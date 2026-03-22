def trapezoidal(f, a, b, n):
    """
    f: function to integrate
    a: lower bound
    b: upper bound    n: number of intervals
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)] # list of x values
    y = [f(x[i]) for i in range(n + 1)]   # list of y values
    s = y[0] + y[n]
    for i in range(1, n):
        s += 2 * y[i]
    return s * h / 2        # the formula of trapezoidal rule

def f(x):
    """defines the integrand"""
    return x ** 4 - 2 * x + 1

def F(x):
    """defines the integral of f(x) from 0 to x"""
    return x ** 5 / 5 - x ** 2 + x

def approxE(x, n):
    """defines the integral of f(x) from 0 to x"""
    return trapezoidal(f, 0, x, n)


realValue = F(2)
print(f"Real value of E(2): {realValue}")

result10 = approxE(2, 10)
print(f"Approximation with 10 intervals: {result10}")
result20 = approxE(2, 20)
print(f"Approximation with 20 intervals: {result20}")

estError = abs(result10 - result20) / 3
realError = abs(result10 - realValue)

print(f"Estimated error: {estError}")
print(f"Real error: {realError}")
