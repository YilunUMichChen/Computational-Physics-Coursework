import math
import numpy as np
import matplotlib.pyplot as plt

# Initialize variables
D = {} #The dictionary stores N as keys and results as values
Errors = {}  #The dictionary stores N as keys and errors as values

# Define the function xloop to calculate x for different N values
def xloop():
    # Loop through N from 10 to 100
    for N in range(10, 101):
        # Reset x to 1/2 at the start of each N iteration
        x = 1/2
        # Perform N nested calculations
        for _ in range(1, N + 1):
            x = 1 / (2 + x)
        # print(f'When N = {N}, x = {x}')
        # Store the current N and x in dictionary D
        D[N] = 1 + x
        Errors[N] = abs((1+x) - math.sqrt(2))


xloop()



# Extract N values and corresponding results
N_values = list(D.keys())
result_values = list(D.values())
# Transform into arrays
N_values = np.array(N_values)
result_values = np.array(result_values)



# Plot the results as a function of N
plt.figure(figsize=(10, 6))
plt.plot(N_values, result_values)
plt.title('Results vs N')
plt.xlabel('N')
plt.ylabel('Result (x)')
plt.grid(True)


# Show the plot
plt.show()




# Extract N values and corresponding errors
N_values = list(Errors.keys())
error_values = list(Errors.values())
# Transform into arrays
N_values = np.array(N_values)
error_values = np.array(error_values)



# Plot the errors as a function of N
plt.figure(figsize=(10, 6))
plt.plot(N_values, error_values)
plt.title('Errors vs N')
plt.xlabel('N')
plt.ylabel('Error (x)')
plt.grid(True)


# Show the plot
plt.show()