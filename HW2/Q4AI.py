import numpy as np
import matplotlib.pyplot as plt

# Define forward difference function
def fd(f, x, h):
    return (f(x + h) - f(x)) / h

# Define central difference function
def cd(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Define true derivative of cos(x)
def td_cos(x):
    return -np.sin(x)

# Define true derivative of exp(x)
def td_exp(x):
    return np.exp(x)

# Define cos(x) function
def f_cos(x):
    return np.cos(x)

# Define exp(x) function
def f_exp(x):
    return np.exp(x)

# Given x values
x_vals = [0.1, 1, 100]
h_vals = []

# Initialize the error lists as two-dimensional lists, where each sub-list corresponds to an x value.
fe_cos = [[] for _ in x_vals]
ce_cos = [[] for _ in x_vals]
fe_exp = [[] for _ in x_vals]
ce_exp = [[] for _ in x_vals]

h = 1
while h >= 1e-16:
    h_vals.append(h)
    for i, x in enumerate(x_vals):
        # Calculate forward and central derivative for cos(x)
        fd_cos = fd(f_cos, x, h)
        cd_cos = cd(f_cos, x, h)
        td_cos_val = td_cos(x)
        # Calculate the relative error: divide absolute error by the absolute value
        fe_cos_val = np.abs((fd_cos - td_cos_val) / td_cos_val) if td_cos_val != 0 else 0
        ce_cos_val = np.abs((cd_cos - td_cos_val) / td_cos_val) if td_cos_val != 0 else 0

        # Calculate forward and central derivative for exp(x)
        fd_exp = fd(f_exp, x, h)
        cd_exp = cd(f_exp, x, h)
        td_exp_val = td_exp(x)
        fe_exp_val = np.abs((fd_exp - td_exp_val) / td_exp_val) if td_exp_val != 0 else 0
        ce_exp_val = np.abs((cd_exp - td_exp_val) / td_exp_val) if td_exp_val != 0 else 0

        # Add the error data to the corresponding sub - lists.
        fe_cos[i].append(fe_cos_val)
        ce_cos[i].append(ce_cos_val)
        fe_exp[i].append(fe_exp_val)
        ce_exp[i].append(ce_exp_val)

    h /= 10

# change lists into arrays
h_vals = np.array(h_vals)
fe_cos = np.array(fe_cos)
ce_cos = np.array(ce_cos)
fe_exp = np.array(fe_exp)
ce_exp = np.array(ce_exp)

# Plot error for cos(x)
for i, x in enumerate(x_vals):
    plt.figure()
    plt.loglog(h_vals, fe_cos[i], label='Forward Difference Error')
    plt.loglog(h_vals, ce_cos[i], label='Central Difference Error')
    plt.xlabel('Step Size h')
    plt.ylabel('Relative Error')
    plt.title(f'Error vs h for f(x) = cos(x) at x = {x}')
    plt.legend()
    plt.show()

# Plot error for exp(x)
for i, x in enumerate(x_vals):
    plt.figure()
    plt.loglog(h_vals, fe_exp[i], label='Forward Difference Error')
    plt.loglog(h_vals, ce_exp[i], label='Central Difference Error')
    plt.xlabel('Step Size h')
    plt.ylabel('Relative Error')
    plt.title(f'Error vs h for f(x) = exp(x) at x = {x}')
    plt.legend()
    plt.show()