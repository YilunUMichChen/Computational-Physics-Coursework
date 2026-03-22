from math import sin,cos,tan
import matplotlib.pyplot as plt
import numpy as np

real_value = -0.0834375

#Define central difference for the 2nd order derivative
def d2f_central(f,x,h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

#Define function of x
def f(x):
    return (1 - np.cos(x)) / (x ** 2)

log_h = np.array([-1.0,-2.0,-3.0,-4.0,-5.0,-6.0])
#important: define the element as float number to allow the non-integer result when doing operations on the elements of the array

y = d2f_central(f, 0.004, 10 ** (log_h))  #values of the function

error = abs(y - real_value)    #values of the absolute error

log_error = np.log10(error)    #log values of the absolute error


#make a log-log plot of error vs h
plt.xlabel("log_h")
plt.ylabel("log_error")

plt.grid(True)
plt.plot(log_h,log_error)
plt.show()


#simplified function after changing the form of the numerator using trigonometric identity 
def simplifiedf(x):
    return 2 * ((np.sin(x / 2)) ** 2) / (x ** 2)



log_h = np.array([-1.0,-2.0,-3.0,-4.0,-5.0,-6.0])
#important: define the element as float number to allow the non-integer result when doing operations on the elements of the array

y = d2f_central(simplifiedf, 0.004, 10 ** (log_h))    #values of the function

error = abs(y - real_value)    #values of the absolute error

log_error = np.log10(error)    #log values of the absolute error


#make a log-log plot of error vs h
plt.xlabel("log_h")
plt.ylabel("log_error")

plt.grid(True)
plt.plot(log_h,log_error)
plt.show()