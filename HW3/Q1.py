"""Use Simpson's rule to evaluate the integral of f(x)"""
from math import exp
import matplotlib.pyplot as plt
def simpson(f, a, b, n):
    """
    f: function to integrate
    a: lower bound
    b: upper bound    n: number of intervals (must be even)
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)] # list of x values
    y = [f(x[i]) for i in range(n + 1)]   # list of y values
    s = y[0] + y[n]
    for i in range(1, n):   
        if i % 2 == 0:
            s += 2 * y[i]   # even terms with coefficient 2
        else:
            s += 4 * y[i]   # odd terms with coefficient 4
    return s * h / 3        # the formula of Simpson's rule

def f(x):
    """defines the integrand"""
    return exp(-x**2)

def approxE(x):
    """defines the integral of f(x) from 0 to x"""
    return simpson(f, 0, x, 1000)  

def main1():
    """main function"""
    results = {}
    i = 0
    while True:
        if i >= 3.1:
            break
        i = round(i, 1)  # round to 1 decimal place to avoid floating point errors
        results[i] = approxE(i)
        i += 0.1
    print(results)
    return results

xyresults = main1()    

main1()

'''Plot E(x) vs x'''
# Extract x and y values from the dictionary
x_values = list(xyresults.keys())
y_values = list(xyresults.values())

# Plot the graph
plt.plot(x_values, y_values, 'o')
plt.title('$E(x)$ vs $x$')
plt.xlabel('$x$')
plt.ylabel('$E(x)$')
plt.grid(True)
plt.show()