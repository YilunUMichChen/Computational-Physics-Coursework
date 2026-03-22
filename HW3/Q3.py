import numpy as np
import matplotlib.pyplot as plt

def left_rectangle(a, b, n):
    """
    a: lower bound
    b: upper bound
    n: number of intervals
    """
    h = (b - a) / n
    x = np.linspace(a, b - h, n)
    integral = h * np.sum(f(x))
    return integral

def trapezoidal(a, b, n):
    """
    a: lower bound
    b: upper bound
    n: number of intervals
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h / 2 * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    return integral

def adaptive_trapezoidal(a, b, tol):
    """
    a: lower bound
    b: upper bound
    tol: tolerance
    """
    n = 1
    T1 = trapezoidal(a, b, n)
    T2 = trapezoidal(a, b, 2 * n)
    error = np.abs(T2 - T1) / 3
    while error > tol:
        n *= 2
        T1 = T2
        T2 = trapezoidal(a, b, 2 * n)
        error = np.abs(T2 - T1) / 3
    return T2, n


def adaptive_trapezoidal(a, b, tol):
    """
    a: lower bound
    b: upper bound
    tol: tolerance
    """
    n = 1
    T1 = trapezoidal(a, b, n)
    T2 = trapezoidal(a, b, 2 * n)
    error = np.abs(T2 - T1) / 3
    while error > tol:
        n *= 2
        T1 = T2
        T2 = trapezoidal(a, b, 2 * n)
        error = np.abs(T2 - T1) / 3
    return T2, n


def simpson(a, b, n):
    """
    a: lower bound
    b: upper bound
    n: number of intervals
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = h / 3 * (y[0] + 4 * np.sum(y[1::2]) + 2 * np.sum(y[2:-1:2]) + y[n])
    return integral

def adaptive_simpson(a, b, tol):
    """
    a: lower bound
    b: upper bound
    tol: tolerance
    """
    n = 2
    S1 = simpson(a, b, n)
    S2 = simpson(a, b, 2 * n)
    error = np.abs(S2 - S1) / 15
    while error > tol:
        n *= 2
        S1 = S2
        S2 = simpson(a, b, 2 * n)
        error = np.abs(S2 - S1) / 15
    return S2, n


def romberg(f, a, b, accuracy=1e-4, max_order=100):
    """
    Calculate the integral f using the Romberg integration method.

    Parameters:
    f -- The function to be integrated
    a -- The lower limit of the integration interval.
    b -- The upper limit of the integration interval.
    accuracy -- The desired accuracy of the integration result, default is 1e-4.
    max_order -- The maximum number of iterations, default is 100.

    Returns:
    The integration result that meets the accuracy requirement. 
    If the accuracy is not achieved, return the last iteration result.
    """
    # Create a 2D array R to store the values in the Romberg integration table
    R = np.zeros((max_order, max_order))

    # Calculate the initial step size h by dividing the interval [a, b] into two parts
    h = (b - a) / 2.
    # Use the trapezoidal rule to calculate the initial integral approximation
    R[0, 0] = h * (f(a) + f(b))  

    # Outer loop: Increase the degree of subdivision of the trapezoidal rule step by step
    for n in range(1, max_order):
        trapezoid = 0.0
        # Inner loop: Calculate the sum of function values for the new trapezoids 
        # in the current degree of subdivision
        for j in range(2 ** (n - 1)):
            trapezoid += f(a + (2 * j + 1) * h)
        # Update the first column of the Romberg integration table 
        # (integral values of the trapezoidal rule with different subdivisions)
        R[n, 0] = 0.5 * R[n - 1, 0] + h * trapezoid  

        l = 1
        # Romberg iterations: Improve the accuracy of the integral step by step 
        # through linear combinations of integral values from previous steps
        for m in range(1, n + 1):
            l *= 4
            R[n, m] = (l * R[n, m - 1] - R[n - 1, m - 1]) / (l - 1)
            print("Iteration: {0:5}, I = {1:20.15f}, error estimate = {2:10.15f}".format(n, R[n, m], abs(R[n, m] - R[n - 1, m - 1])))
            # Check if the current iteration meets the specified accuracy
            if abs(R[n, m] - R[n - 1, m - 1]) < accuracy:
                return R[n, m]
        # Halve the step size h for further subdivision of the interval 
        # in the next iteration
        h /= 2.

    print("Romberg method did not converge to required accuracy")
    # Return the last calculated value in the integration table 
    # if the accuracy is not achieved
    return R[-1, -1]


def mid_rectangle_rule(f, a, b, n):
    """
    f: function to integrate
    a: lower bound
    b: upper bound
    n: number of intervals
    """
    h = (b - a) / n
    ret = 0.0
    xk = a + h / 2.
    for k in range(n):
        ret += f(xk) * h
        xk += h
    return ret

# def f(x):
#     """defines the integrand"""
#     # deal with the singularity at x = 0
#     eps = 1e-10  # small value to avoid division by zero
#     if np.isscalar(x):
#         if np.abs(x) < eps:
#             return 1 / np.sqrt(x) - 2 * np.sqrt(x) if x > 0 else 0
#         return (np.cos(x) - 2 * np.sin(x)) / np.sqrt(x)
#     mask = np.abs(x) < eps
#     result = np.zeros_like(x)
#     # use the original function for non-zero values of x
#     result[~mask] = (np.cos(x[~mask]) - 2 * np.sin(x[~mask])) / np.sqrt(x[~mask])
#     # use Taylor series expansion for small x
#     valid_mask = mask & (x > 0)
#     result[valid_mask] = 1 / np.sqrt(x[valid_mask]) - 2 * np.sqrt(x[valid_mask])
#     return result



def f(t):
    """
    Defines the integrand after variable substitution x = t^2.
    """
    return 2 * ((np.cos(t ** 2) - 2 * np.sin(t ** 2)))

tol = 1e-4
print(tol)




integral_trap, n_trap = adaptive_trapezoidal(0, 1, tol)
print("Number of intervals for adaptive trapezoidal rule:", n_trap)
print("Integral using adaptive trapezoidal rule:", integral_trap)

integral_simp, n_simp = adaptive_simpson(0, 1, tol)
print("Number of intervals for adaptive Simpson's rule:", n_simp)
print("Integral using adaptive Simpson's rule:", integral_simp)

"""Calculate integral using left rectangle rule with increasing number of intervals until convergence within tolerance is achieved"""
n_rect = []
integral_rect = []
i0 = 2
while True:
    integral = left_rectangle(0, 1, i0)
    n_rect.append(i0)
    integral_rect.append(integral)
    if len(integral_rect) > 0 and np.abs(integral - integral_trap) < tol:
        #compare the integral with the integral from trapezoidal rule, if the difference is less than the tolerance, then we have converged
        break
    i0 *= 2

print("Number of intervals for left-hand rectangle rule:", n_rect[-1])
print("Integral using left-hand rectangle rule:", integral_rect[-1])

integral_romberg = romberg(f, 0, 1, accuracy=tol)
print("Integral using Romberg integration:", integral_romberg)


"""plot the results for the left-hand rectangle rule"""
plt.plot(n_rect, integral_rect, label='Left-hand rectangle rule')
plt.xlabel('Number of intervals')
plt.ylabel('Integral')
plt.title('Left-hand rectangle rule')
plt.legend()
plt.show()



"""plot showing the integral value vs. number of slices for the trapezoidal rule"""
n_t = 1
n_t_values = []
integral_trap_values = []
while n_t <= n_trap:
    integral_trap = trapezoidal(0, 1, n_t)
    n_t_values.append(n_t)
    integral_trap_values.append(integral_trap)
    n_t = 2 * n_t
plt.plot(n_t_values, integral_trap_values, 'o', color='blue',linestyle='-')
plt.xlabel('Number of intervals')
plt.ylabel('Integral')
plt.title('Trapezoidal rule')
plt.show()
    
    



"""plot showing the integral value vs. number of slices for the Simpson's rule"""
n_s = 1
n_s_values = []
integral_simp_values = []
while n_s <= n_simp:
    integral_simp = simpson(0, 1, n_s)
    n_s_values.append(n_s)
    integral_simp_values.append(integral_simp)
    n_s = 2 * n_s

plt.plot(n_s_values, integral_simp_values, 'o', color='green', linestyle='-')
plt.xlabel('Number of intervals')
plt.ylabel('Integral')
plt.title('Simpson\'s rule')
plt.show()





def romberg_for_plot(f, a, b, accuracy=1e-4, max_order=100):
    """
    Perform Romberg integration to calculate the definite integral of a function f from a to b, 
    and record the integral values and slice counts at each step, in order to plot the integral value vs. number of slices.

    Parameters:
    f -- The function to be integrated.
    a -- The lower limit of the integration interval.
    b -- The upper limit of the integration interval.
    accuracy -- The desired accuracy for the integration result. Default is 1e-4.
    max_order -- The maximum number of iterations. Default is 100.

    Returns:
    A tuple containing two lists:
    - integral_values: A list of integral values calculated at each step.
    - slice_counts: A list of the number of slices used at each step.
    """
    # Initialize the Romberg matrix
    R = np.zeros((max_order, max_order))
    # Calculate the initial step size
    h = (b - a) / 2.
    # Calculate the initial integral value using the trapezoidal rule
    R[0, 0] = h * (f(a) + f(b))

    # Initialize lists to store slice counts and integral values
    slice_counts = [2]  # Initial number of slices is 2
    integral_values = [R[0, 0]]  # Initial integral value

    for n in range(1, max_order):
        # Calculate the sum for the trapezoidal rule
        trapezoid = 0.0
        for j in range(2 ** (n - 1)):
            trapezoid += f(a + (2 * j + 1) * h)
        # Update the first column of the Romberg matrix using the trapezoidal rule
        R[n, 0] = 0.5 * R[n - 1, 0] + h * trapezoid

        l = 1
        for m in range(1, n + 1):
            # Update the coefficient for the Romberg extrapolation
            l *= 4
            # Perform Romberg extrapolation
            R[n, m] = (l * R[n, m - 1] - R[n - 1, m - 1]) / (l - 1)
            # Print iteration information
            print("Iteration: {0:5}, I = {1:20.15f}, error estimate = {2:10.15f}".format(n, R[n, m], abs(R[n, m] - R[n - 1, m - 1])))
            # Check if the desired accuracy is achieved
            if abs(R[n, m] - R[n - 1, m - 1]) < accuracy:
                # Record the current number of slices
                slice_counts.append(2 ** n)
                # Record the current integral value
                integral_values.append(R[n, m])
                return integral_values, slice_counts

        # Halve the step size for the next iteration
        h /= 2.
        # Record the number of slices for the next step
        slice_counts.append(2 ** (n + 1))
        # Record the integral value from the trapezoidal rule at this step
        integral_values.append(R[n, 0])

    print("Romberg method did not converge to required accuracy")
    return integral_values, slice_counts


"""plot showing the integral value vs. number of slices for Romberg's method"""
# Call the romberg function to get integral values and slice counts
integral_values, slice_counts = romberg_for_plot(f, 0, 1)

# Plot the integral value against the number of slices
plt.plot(slice_counts, integral_values, marker='o')
plt.xlabel('Number of Slices')
plt.ylabel('Integral Value')
plt.title('Romberg Integration: Integral Value vs Number of Slices')
plt.show()



