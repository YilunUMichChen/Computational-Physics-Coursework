import numpy as np


'''the gaussxw.py file is extracted(cited) from the example code called
HighOrderIntegration_code_examples.ipynb of PHY2650 on the Blackboard'''
from gaussxw import gaussxwab #Make sure to have gaussxw.py in the same directory!!!!!!

def integrand_original(x):
    '''The integrand for the original integral'''
    return x**3 / (np.exp(x) - 1)

def integrand_modified(t):
    '''
    Use the change of variables t = e ^ (-x) to transform the original integral
    After the change of variables, the integrand becomes np.log(t) ** 3 / (1 - t)
    the limits of integration are from 1 to 0'''
    return np.log(t) ** 3 / (1 - t)

def calculate_integral(N):
    '''
    Calculate the integral of integrand_modified(t) from 0 to 1
    using Gaussian quadrature with N sample points
    '''
    # Use the exact interval [0,1] as Gaussian quadrature won't choose endpoints
    # Get Gaussian-Legendre quadrature nodes and weights
    x, w = gaussxwab(N, 1.0, 0.0) # Note that after change of variables, the limits are [1,0] instead of [0,1]
    
    # Calculate the integral
    s = 0.0
    for i in range(N):
        s += w[i] * integrand_modified(x[i])
    
    return s

# Calculate the integral using different numbers of sample points
N_values = [10, 20, 50, 100, 1000]
for N in N_values:
    integral_value = calculate_integral(N)
    print(f"Integral value using {N} sample points: {integral_value}")

# Display the final result (using the maximum number of sample points)
final_result = calculate_integral(1000)
print(f"\nFinal integral result using 1000 sample points: {final_result}")

# This integral has an exact value of pi^4/15, which can be compared
theoretical = np.pi**4/15
print(f"Theoretical value: {theoretical}")
print(f"Relative error: {abs(final_result-theoretical)/theoretical:.8f}")
print(f"Accuracy: {1-abs(final_result-theoretical)/theoretical:.8f}")

'''Then we may compute the Stefan-Boltzmann constant using the integral and the 
Stefan's law: W = sigma * T^4'''
# Define physical constants
k_B = 1.380649e-23  # Boltzmann constant in J/K
c = 2.99792458e8    # Speed of light in m/s
h = 6.62607015e-34  # Planck's constant
hbar = h / (2 * np.pi)  # Reduced Planck's constant 
pi = np.pi

# Compute the coefficient: k_B^4 / (4 * pi^2 * c^2 * hbar^3)
numerator = k_B**4
denominator = 4 * pi**2 * c**2 * hbar**3
coefficient = numerator / denominator

print()

#Hence the Stefan-Boltzmann constant is given by:
estimated_stefan_boltzmann_constant = coefficient * final_result
print(f"Estimated Stefan-Boltzmann constant: {estimated_stefan_boltzmann_constant:.8e} J/((m^2)(K^4))")
# This value can be compared with the known value of the Stefan-Boltzmann constant in SI units, which is approximately 5.670374419e-8 J/(m^2·K^4).
# The relative error can be calculated as follows:
print("Known Stefan-Boltzmann constant: 5.670374419e-8 J/((m^2)(K^4))")
relative_error = abs(estimated_stefan_boltzmann_constant - 5.670374419e-8) / 5.670374419e-8
print(f"Relative error: {relative_error:.8f}")