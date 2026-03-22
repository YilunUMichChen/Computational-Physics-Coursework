from math import sin,cos,tan
import matplotlib.pyplot as plt
import numpy as np

#d2f = 4 * (e ** (sin(2 * x))) * ((cos(2 * x)) ** 2 - sin(2 * x))
x = 0.5
real_value = 4 * (np.exp(sin(2 * x))) * ((cos(2 * x)) ** 2 - sin(2 * x))
#use np.exp() instead of np.e **(), otherwise at h = 10e-9, the error will be the same as h = 10e-8 (weird phenomenon)
print(f'the real value at x = {x} is {real_value}')

def d2f_central(f,x,h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)


def f(x):
    return np.exp(np.sin(2 * x))
#use np.exp() instead of np.e **(), otherwise at h = 10e-9, the error will be the same as h = 10e-8 (weird phenomenon)


log_h = np.array([-1.0,-2.0,-3.0,-4.0,-5.0,-6.0,-7.0,-8.0,-9.0,-10.0])
#important: define the element as float number to allow the non-integer result when doing operations on the elements of the array

y = d2f_central(f, x, 10 ** (log_h))

error = abs(y - real_value)

log_error = np.log10(error)


#make a table of error vs. h
print("Log of h\tAbsolute Error")
for h, error in zip(log_h, error):
    print(f"{h}\t\t{error}")




#make a error vs. log_h plot of error vs h
plt.xlabel("Log of h")
plt.ylabel("Log of error")

plt.grid(True)
plt.plot(log_h,log_error)
plt.show()