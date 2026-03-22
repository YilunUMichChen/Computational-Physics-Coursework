import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(np.sin(2 * x))

def second_derivative_central_difference(x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def true_second_derivative(x):
    return 4 * np.exp(np.sin(2 * x)) * (np.cos(2 * x) ** 2 - np.sin(2 * x))

x = 0.5
h_values = np.logspace(-1, -10, 10)
absolute_errors = []

for h in h_values:
    approx_derivative = second_derivative_central_difference(x, h)
    true_derivative = true_second_derivative(x)
    absolute_error = np.abs(approx_derivative - true_derivative)
    absolute_errors.append(absolute_error)

print("h\t\tAbsolute Error")
for h, error in zip(h_values, absolute_errors):
    print(f"{h}\t{error}")

plt.loglog(h_values, absolute_errors)
plt.xlabel('Step - size (h)')
plt.ylabel('Absolute Error')
plt.title('Absolute Error of Second - Derivative Central - Difference Approximation')
plt.show()