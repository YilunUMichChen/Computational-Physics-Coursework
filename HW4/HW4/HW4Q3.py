import numpy as np
import matplotlib.pyplot as plt

'''the gaussxw.py file is extracted(cited) from the example code called
HighOrderIntegration_code_examples.ipynb of PHY2650 on the Blackboard'''
from gaussxw import gaussxwab #Make sure to have gaussxw.py in the same directory!!!!!!


def integrand(x):
    return x**(-1/4) / (np.exp(x) + 2)

def modified_integrand(t):
    '''Usethe change of variable of x = t**4 to avoid the singularity at x = 0
    for the method of adaptive Simpson's rule'''
    return (4 * t**2)/(np.exp(t**4) + 2)


def simpson(a, b, n, integrand):
    """
    a: lower bound
    b: upper bound
    n: number of intervals
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = integrand(x)
    return h / 3 * (y[0] + 4 * np.sum(y[1::2]) + 2 * np.sum(y[2:-1:2]) + y[n])

def adaptive_simpson(a, b, integrand, tol=1e-5):
    """
    a: lower bound
    b: upper bound
    tol: tolerance
    """
    n = 2
    S1 = simpson(a, b, n, integrand)
    S2 = simpson(a, b, 2 * n, integrand)
    error = np.abs(S2 - S1) / 15
    while error > tol:
        n *= 2
        S1 = S2
        S2 = simpson(a, b, 2 * n, integrand)
        error = np.abs(S2 - S1) / 15
    return S2, n

def gaussian_quadrature(a, b, integrand, tol=1e-5):
    """
    Compute integral using Gaussian quadrature
    a: lower bound
    b: upper bound
    integrand: function to integrate
    tol: tolerance
    """
    n = 10  # Start with 10 points
    old_result = 0
    error = float('inf')
    
    while error > tol:
        # Get sample points and weights
        x, w = gaussxwab(n, a, b)
        
        # Compute the integral
        result = np.sum(w * integrand(x))
        
        # Compute error
        error = np.abs(result - old_result)
        
        # Update for next iteration
        old_result = result
        n *= 2
        
        # Safety check to prevent infinite loop
        if n > 1000:
            break
    
    return result, n


'''Question3 Part(1)'''



adaptive_simpson_result, n_simpson = adaptive_simpson(0, 1, modified_integrand, tol=1e-5)
gaussian_quadrature_result, n_gauss = gaussian_quadrature(0, 1, integrand, tol=1e-5)
print(f"Adaptive Simpson's Rule Result: {adaptive_simpson_result}, Number of intervals: {n_simpson}")
print(f"Gaussian Quadrature Result: {gaussian_quadrature_result}, Number of points: {n_gauss}")


'''Question3 Part(2)'''

'''Using the uniform sampling method to estimate the integral'''
def uniform_sampling_integral(a, b, integrand, n_samples):
    '''
    a: lower bound
    b: upper bound
    integrand: function to integrate
    n_samples: number of samples
    '''
    x_samples = np.random.uniform(a, b, n_samples)
    integral_value = (b - a) / n_samples * np.sum(integrand(x_samples))
    return integral_value

uniform_sampling_integral_result = uniform_sampling_integral(0, 1, modified_integrand, 10000)
print(f"Uniform Sampling Result: {uniform_sampling_integral_result}")



'''Using importance sampling to estimate the integral'''

'''After Choosing the Weight Function and Inverse Transform Derivation fro Importance Sampling,
we derive the final estimator for the integral'''

def is_estimator_for_specific_integrand(n_samples):
    '''
    n_samples: number of samples
    '''
    u = np.random.uniform(0, 1, n_samples)
    
    x = u**(4/3)

    weights = (4/3) * (1 / (np.exp(x) + 2))

    I_estimate = np.mean(weights)
    
    return I_estimate


is_estimator_result = is_estimator_for_specific_integrand(10000)
print(f"Importance Sampling Result: {is_estimator_result}")


'''Plot the results vs the number of samples for uniform sampling and importance sampling'''
sample_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
uniform_results = []
importance_results = []
uniform_errors = []
importance_errors = []

reference = adaptive_simpson_result

n_trials = 20
for n in sample_sizes:
    uni_results = []
    for _ in range(n_trials):
        uni_results.append(uniform_sampling_integral(0, 1, integrand, n))
    uniform_results.append(np.mean(uni_results))
    uniform_errors.append(np.std(uni_results))
    
    imp_results = []
    for _ in range(n_trials):
        imp_results.append(is_estimator_for_specific_integrand(n))
    importance_results.append(np.mean(imp_results))
    importance_errors.append(np.std(imp_results))


plt.style.use('default')# Use default style for the plot(white instead of dark background)
plt.figure(figsize=(10, 6), facecolor='white')
plt.plot(sample_sizes, uniform_results, 'o-', label='Uniform Sampling', color='blue')
plt.plot(sample_sizes, importance_results, 'o-', label='Importance Sampling', color='red')

plt.xscale('log')
plt.xlabel('Number of Samples')
plt.ylabel('Integral Estimate')
plt.title('Comparison of Integration Methods')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('sampling_comparison.png', facecolor='white')
plt.show()


'''Use MCMC (Markov chain Monte Carlo) to calculate the results 
and show the final result with error.'''

def mcmc_integration(integrand, n_samples, burn_in=1000, step_size=0.1):
    '''
    Use Metropolis-Hastings algorithm for MCMC integration
    
    Parameters:
    integrand: function to integrate
    n_samples: number of samples to generate
    burn_in: number of initial samples to discard
    step_size: size of the random walk step
    '''
    # Initialize the chain at a random position (avoid starting at 0 due to singularity)
    current_x = np.random.uniform(0, 1)
    samples = []
    
    # Define target distribution proportional to integrand
    # For importance sampling, we want to sample more heavily where integrand is large
    def target_dist(x):
        return integrand(x)
        
    
    # Run the Metropolis-Hastings algorithm
    for i in range(n_samples + burn_in):
        # Propose a new position
        proposed_x = current_x + np.random.normal(0, step_size)
        
        # Reflect proposals outside [0,1] back into the interval
        if proposed_x < 0:
            proposed_x = -proposed_x
        elif proposed_x > 1:
            proposed_x = 2 - proposed_x
        
        # Acceptance probability based on the target distribution
        if 0 <= proposed_x <= 1:
            try:
                acceptance_ratio = target_dist(proposed_x) / target_dist(current_x)
                if np.random.random() < acceptance_ratio:
                    current_x = proposed_x
            except:
                # Handle division errors
                pass
        
        # Store the sample after burn-in
        if i >= burn_in:
            samples.append(current_x)
    
    samples = np.array(samples)
    
    # Calculate integral estimate
    # For uniform target over [0,1], integral = mean(f(x))
    # For non-uniform target, need to correct for sampling bias
    weights = 1.0 / np.array([target_dist(x) for x in samples])
    weights = weights / np.sum(weights)  # Normalize weights
    integral_estimate = np.sum(weights * integrand(samples))
    
    return integral_estimate, samples

# Perform MCMC integration with multiple trials to estimate error
mcmc_trials = 10
mcmc_results = []
for _ in range(mcmc_trials):
    result, _ = mcmc_integration(modified_integrand, n_samples=100000, burn_in=5000)
    mcmc_results.append(result)

mcmc_mean = np.mean(mcmc_results)
mcmc_error = np.std(mcmc_results)

print(f"MCMC Integration Result: {mcmc_mean:.8f} ¡À {mcmc_error:.8f}")


