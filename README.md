# Computational Physics & AI Tools (PHY 2650) - Coursework

## Overview
This repository contains my programming assignments, numerical simulation scripts, and mathematical derivations for the **PHY 2650: Computational Physics and AI Tools** course. The projects here demonstrate the application of advanced numerical methods and computational techniques to solve classical, statistical, and quantum physics problems.

*(Note: The final course project on the Machine Learning Classification of the 2D Ising Model has been uploaded to a separate dedicated repository on my profile.)*

## Tech Stack & Libraries
- **Core Language:** Python 3
- **Scientific Computing:** `NumPy`, `SciPy` (for quadrature and optimization)
- **Data Visualization:** `Matplotlib`
- **Techniques:** Monte Carlo Simulations, Markov Chain Monte Carlo (MCMC), Numerical Integration/Differentiation, Importance Sampling, Bayesian Inference.

## Repository Structure & Topics Covered

Here is a detailed breakdown of the assignments included in this repository:

### `HW1/` : Error Analysis & Lattice Physics
- **Physics Problem:** Calculating the Madelung constant for crystal lattices.
- **Computational Methods:** Implemented numerical summation loops and conducted rigorous computational error bounds analysis (Relative/Absolute errors, Taylor series approximations).

### `HW2/` : Numerical Differentiation
- **Physics Problem:** Analyzing precision limits in continuous functions.
- **Computational Methods:** Implemented **Forward Difference** and **Central Difference** formulas. Investigated the relationship between step size ($h$) and computational error to find the optimal balance between truncation error and round-off error.

### `HW3/` : Fundamental Numerical Integration
- **Computational Methods:** Developed custom implementations of the **Adaptive Simpson's Rule** and the **Romberg Integration Method** to achieve high-precision area calculations under continuous functions.

### `HW4/` : Advanced Integration & Monte Carlo Methods
- **Physics Problems:** 1. Solid-state physics: Evaluating the heat capacity integral (Debye model).
  2. Blackbody radiation: Computing the Stefan-Boltzmann constant.
  3. Geometry: Estimating the volume of the intersection between a sphere and a cylinder.
- **Computational Methods:** - **Gaussian Quadrature** (with variables substitution to handle integration limits).
  - **Importance Sampling** and dealing with integrand singularities via weight functions.
  - **Monte Carlo Volume Estimation** with uncertainty/variance analysis.

### `HW5/` : Statistical Mechanics & Bayesian Statistics
- **Physics Problem:** Simulating the 2D Ising model on a square periodic lattice.
- **Computational Methods:** - Used **MCMC (Metropolis algorithm)** to compute Energy, Magnetization, Heat Capacity, and Susceptibility across various temperatures.
  - **Bayesian Inference:** Mathematical derivation of the posterior and predictive distributions for Bayesian Linear Regression models.

## How to Run
The code is organized into separate Python scripts for each homework question (e.g., `HW4Q1.py`, `HW4Q2.py`). To run a specific simulation, execute the script via your terminal:

`python HW4Q1.py`

*For detailed mathematical derivations and error analysis plots, please refer to the accompanying PDF reports in each homework directory.*

## Academic Integrity
These files are provided for portfolio showcase and research application purposes. If you are a current student taking this course, please adhere to your university's academic integrity policies and do not copy this code for your own assignments.
