import math
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the n-th term of the Taylor series for sin(x)
def taylorSineTerm(x, n):
    return ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

# Function to calculate the error of the Taylor series approximation of sin(x) up to N terms
def taylorExpansionOfSin(x,N):
    sum_result = 0
    n = 0
    while n <= N:
        term = taylorSineTerm(x, n)
        sum_result += term
        n += 1
    error = abs(sum_result - math.sin(x))
    return error


# List of x values to calculate errors for
x_values = [0.5, 1, 2, 5, 10]

for x in x_values:
    N_values = []
    Error_values = []
    max_N = 20
    
    # Calculate errors for different numbers of terms (N)
    for N in range(1,max_N):
        error = taylorExpansionOfSin(x,N)
        N_values.append(N)
        Error_values.append(error)
    
    N_values = np.array(N_values)
    Error_values = np.array(Error_values)
    
    plt.plot(N_values, Error_values, label=f'x = {x}')

plt.xlabel('N')
plt.ylabel('Error')

plt.xticks(range(0, max_N + 1, 1))   # Set x-axis tick marks
plt.ylim(0, 0.3)

plt.title('Error vs N for different x values')  # Set y-axis limits
plt.legend()  # Show legend for x with different colors

plt.show()



