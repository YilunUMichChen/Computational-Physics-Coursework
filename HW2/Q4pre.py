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

fe_cos = []  #Forward Difference Error of cosine
ce_cos = []  #Central Difference Error of cosine
fe_exp = []  #Forward Difference Error of exponential
ce_exp = []  #Central Difference Error of exponential

h = 1
while h >= 1e-16:
    h_vals.append(h)
    for x in x_vals:
        # Calculate forward and central derivative for cos(x)
        fd_cos = fd(f_cos, x, h)
        cd_cos = cd(f_cos, x, h)
        td_cos_val = td_cos(x)
        #Calculate the relative error: divide absolute error by the absolute value
        fe_cos_val = np.abs((fd_cos - td_cos_val) / td_cos_val) 
        # if td_cos_val != 0 else 0    #must check if the denominator is zero
        ce_cos_val = np.abs((cd_cos - td_cos_val) / td_cos_val) 
        # if td_cos_val != 0 else 0    #must check if the denominator is zero

        # Calculate forward and central derivative for exp(x)
        fd_exp = fd(f_exp, x, h)
        cd_exp = cd(f_exp, x, h)
        td_exp_val = td_exp(x)
        fe_exp_val = np.abs((fd_exp - td_exp_val) / td_exp_val) 
        # if td_exp_val != 0 else 0    #must check if the denominator is zero
        ce_exp_val = np.abs((cd_exp - td_exp_val) / td_exp_val) 
        # if td_exp_val != 0 else 0    #must check if the denominator is zero

        fe_cos.append(fe_cos_val)
        ce_cos.append(ce_cos_val)
        fe_exp.append(fe_exp_val)
        ce_exp.append(ce_exp_val)

    h /= 10


#change lists into arrays and reshape as a 2D array
h_vals = np.array(h_vals)
print(fe_cos)
fe_cos = np.array(fe_cos).reshape(len(x_vals), -1)
print(fe_cos)
ce_cos = np.array(ce_cos).reshape(len(x_vals), -1)
fe_exp = np.array(fe_exp).reshape(len(x_vals), -1)
ce_exp = np.array(ce_exp).reshape(len(x_vals), -1)

# Plot error for cos(x)
for i, x in enumerate(x_vals):  
    plt.figure()
    plt.loglog(h_vals, fe_cos[i], label='Forward Difference Error')    #index i of fe_cos corresponding to the error of ith x_value 
    plt.loglog(h_vals, ce_cos[i], label='Central Difference Error')    #index i of ce_cos corresponding to the error of ith x_value 
    plt.xlabel('Step Size h')
    plt.ylabel('Relative Error')
    plt.title(f'Error vs h for f(x) = cos(x) at x = {x}')
    plt.legend()    #add legend
    plt.show()

# Plot error for exp(x)
for i, x in enumerate(x_vals):
    plt.figure()
    plt.loglog(h_vals, fe_exp[i], label='Forward Difference Error')    #index i of fe_exp corresponding to error of the ith x_value
    plt.loglog(h_vals, ce_exp[i], label='Central Difference Error')    #index i of fe_exp corresponding to error of the ith x_value
    plt.xlabel('Step Size h')
    plt.ylabel('Relative Error')
    plt.title(f'Error vs h for f(x) = exp(x) at x = {x}')
    plt.legend()    #add legend
    plt.show()