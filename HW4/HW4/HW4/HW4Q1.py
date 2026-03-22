'''Evaluate the heat capacity integral with gaussian quadrature'''
import numpy as np
import matplotlib.pyplot as plt

'''the gaussxw.py file is extracted(cited) from the example code called
HighOrderIntegration_code_examples.ipynb of PHY2650 on the Blackboard'''
from gaussxw import gaussxwab #Make sure to have gaussxw.py in the same directory!!!!!!

# Constants
V = 0.001  # Volume in m^3 (1000 cm^3 = 0.001 m^3)
rho = 6.022e28  # Number density in m^-3
k_B = 1.380649e-23  # Boltzmann constant in J/K
theta_D = 428  # Debye temperature in Kelvin

#Modifiable parameters
N = 50  # Number of Gaussian quadrature points
T = 300  #default temperature


# Calculate the prefactor for the integral
prefactor = 9 * V * rho * k_B * (T / theta_D)**3


def integrand(x):
    '''Integrand for the heat capacity integral'''
    numerator = x**4 * np.exp(x)
    denominator = (np.exp(x) - 1)**2
    return numerator / denominator


def heat_capacity_gaussian_quadrature(V, rho, k_B, T, theta_D, N):
    '''Calculate the heat capacity using Gaussian quadrature
    
    Parameters:
    V : float
        Volume in cubic meters (m^3)
    rho : float
        Number density in m^-3
    k_B : float
        Boltzmann constant in J/K
    T : float
        Temperature in Kelvin
    theta_D : float
        Debye temperature in Kelvin
    N : int
        Number of Gaussian quadrature points
        
    Returns:
    float : Heat capacity in J/K
    '''
    # Calculate the upper limit of the integral (theta_D/T)
    upper_limit = theta_D / T
    
    # Get Gaussian quadrature points and weights
    x, w = gaussxwab(N, 0, upper_limit)
    
    # Calculate the integral using Gaussian quadrature
    integral_sum = 0
    for i in range(N):
        integral_sum += w[i] * integrand(x[i])
    
    # Calculate the prefactor
    prefactor = 9 * V * rho * k_B * (T / theta_D)**3
    
    return prefactor * integral_sum


def cv(T):
    '''
    Calculate the heat capacity for aluminum at a given temperature.
    
    Parameters:
    T : float
        Temperature in Kelvin
    
    Returns:
    float : Heat capacity in J/K
    '''
    # Constants for aluminum sample
    V = 0.001  # Volume in m^3 (1000 cm^3 = 0.001 m^3)
    rho = 6.022e28  # Number density in m^-3
    k_B = 1.380649e-23  # Boltzmann constant in J/K
    theta_D = 428  # Debye temperature in Kelvin
    N = 50  # Number of Gaussian quadrature points
    
    return heat_capacity_gaussian_quadrature(V, rho, k_B, T, theta_D, N)


def plot_heat_capacity():
    '''
    Plot the heat capacity as a function of temperature from 5K to 500K
    with appropriate partitioning to capture the curve behavior.
    '''
    # Create a nonlinear temperature partition with more points at lower temperatures
    # Use logarithmic spacing for temperatures from 5K to ~100K
    T_low = np.logspace(np.log10(5), np.log10(100), 50)
    # Use linear spacing for temperatures from ~100K to 500K
    T_high = np.linspace(100, 500, 30)
    # Combine the two arrays
    temperatures = np.unique(np.concatenate((T_low, T_high)))
    
    # Calculate heat capacity for each temperature
    heat_capacities = [cv(T) for T in temperatures]
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, heat_capacities, 'b-', linewidth=2)
    plt.xlabel('Temperature (K)', fontsize=12)
    plt.ylabel('Heat Capacity (J/K)', fontsize=12)
    plt.title('Heat Capacity of Aluminum vs Temperature', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add a vertical line at the Debye temperature
    plt.axvline(x=theta_D, color='r', linestyle='--', label=f'Debye Temperature = {theta_D} K')
    
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_heat_capacity()


