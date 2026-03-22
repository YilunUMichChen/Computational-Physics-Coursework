import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    '''define the function name as f of x for convenience.'''
    return x**6 + 0.1 * np.log(np.abs(1 + 3 * (1 - x)))

numpoints = 100

x = np.linspace(0.5,1.5,numpoints)

y = f(x)

'''create a plot'''
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.plot(x,y)
plt.show()


'''create a plot with a much finer grid'''
plt.xlabel("x")
plt.ylabel("f(x)")
xticks = np.arange(0.0, 1.6, 0.1)
plt.xticks(xticks)
yticks = np.arange(0.0, 12.0, 0.5)
plt.yticks(yticks)
plt.grid(True)
plt.plot(x,y)
plt.show()
