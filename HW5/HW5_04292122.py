import numpy as np
import matplotlib.pyplot as plt



J = 3

# Energy of 2D Ising system for a given spin configuration
def IsingE(spins, periodicBC = False):
    energy = 0
    N = len(spins)
    for i in range(N):
        for j in range(N):
            if (i > 0 or periodicBC):
                energy += -J * spins[i][j] * spins[i-1][j]
            if (j > 0 or periodicBC):
                energy += -J * spins[i][j] * spins[i][j-1]
            if (i < N - 1 or periodicBC):
                energy += -J * spins[i][j] * spins[(i+1)%N][j]
            if (j < N - 1 or periodicBC):
                energy += -J * spins[i][j] * spins[i][(j+1)%N]
    return energy 

# Magnetization of 2D Ising system for a given spin configuration
def IsingM(spins):
    return np.sum(spins)

# Change of energy of the Ising system by flipping the spin at the location (i,j)
def IsingdEflip(spins, i, j, periodicBC = False):
    N = len(spins)
    dE = 0
    if (i > 0 or periodicBC):
        dE += 2 * J * spins[i][j] * spins[i-1][j]
    if (j > 0 or periodicBC):
        dE += 2 * J * spins[i][j] * spins[i][j-1]
    if (i < N - 1 or periodicBC):
        dE += 2 * J * spins[i][j] * spins[(i+1)%N][j]
    if (j < N - 1 or periodicBC):
        dE += 2 * J * spins[i][j] * spins[i][(j+1)%N]
    return dE

# Simulates the 2D Ising system of NxN spins at temperature T
# by performing Markov chain steps using Metropolis algorithm
# Returns arrays energies and magnetizations at each step
def simulateIsing(T, N, steps, burn_in_steps, periodicBC = False):
    spins = -1 + 2 * np.random.randint(0, high = 2, size=(N,N))
    
    E = IsingE(spins, periodicBC)
    M = IsingM(spins)

    # Energy
    eplot = [ E ]
    # Magnetisation
    Mplot = [ M ]

    for k in range(steps):
        # Pick the lattice site randomly
        i = np.random.randint(N)
        j = np.random.randint(N)
        
        # Energy change from flipping the site
        dE = IsingdEflip(spins, i, j, periodicBC)
        
        # Flip the spin with some probability
        if (np.random.rand() < np.exp(-dE/T)):
            spins[i,j] = -spins[i,j]
            E += dE
            M += 2 * spins[i,j]
        
        if k >= steps - burn_in_steps:
            eplot.append(E)
            Mplot.append(M)
    
    return eplot, Mplot

# Function to calculate observables and plot them
def calculate_and_plot_observables(N, steps, burn_in_steps, periodicBC=False):
    temperatures = np.arange(1, 20.2, 0.2)
    energies = []
    magnetizations = []
    heat_capacities = []
    susceptibilities = []

    for T in temperatures:
        eplot, Mplot = simulateIsing(T, N, steps, burn_in_steps, periodicBC)
        E_avg = np.mean(eplot)
        E2_avg = np.mean(np.square(eplot))
        M_avg = np.mean(Mplot)
        M2_avg = np.mean(np.square(Mplot))

        Cv = (E2_avg - E_avg**2) / (T**2)
        chi = (M2_avg - M_avg**2) / T

        energies.append(E_avg)
        magnetizations.append(M_avg)
        heat_capacities.append(Cv)
        susceptibilities.append(chi)

    # Plotting
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.plot(temperatures, energies, label="Energy")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Energy")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(temperatures, magnetizations, label="Magnetization", color="orange")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Magnetization")
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(temperatures, heat_capacities, label="Heat Capacity", color="green")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Heat Capacity")
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(temperatures, susceptibilities, label="Susceptibility", color="red")
    plt.xlabel("Temperature (T)")
    plt.ylabel("Susceptibility")
    plt.legend()

    plt.tight_layout()
    plt.show()

# Plot
calculate_and_plot_observables(N=12, steps=200000, burn_in_steps=190000, periodicBC=True)