'''Estimate the volume of the intersection of a sphere and a cylinder, using Monte Carlo
approach. The sphere has radius 1 and is centered at the origin. The cylinder has radius
1/2, and its axis is perpendicular to the x axis and goes through the point (1/2, 0, 0).
Report your uncertainty.'''

import numpy as np

def is_in_sphere(point, center=(0, 0, 0), radius=1):
    """Check if a point is inside the sphere"""
    x, y, z = point
    cx, cy, cz = center
    return ((x - cx)**2 + (y - cy)**2 + (z - cz)**2) <= radius**2

def is_in_cylinder(point, axis_point=(0.5, 0, 0), radius=0.5):
    """Check if a point is inside the cylinder"""
    x, y, z = point
    ax, ay, az = axis_point  
    return (x - ax)**2 + (y - ay)**2 <= radius**2

def monte_carlo_volume_estimation(num_points):
    """Estimate intersection volume using Monte Carlo method"""
    # Define a box that contains all possible intersection points
    x_min, x_max = -1, 1.5
    y_min, y_max = -1, 1
    z_min, z_max = -1, 1
    
    # Generate random points
    points_x = np.random.uniform(x_min, x_max, num_points)
    points_y = np.random.uniform(y_min, y_max, num_points)
    points_z = np.random.uniform(z_min, z_max, num_points)
    
    points = np.column_stack((points_x, points_y, points_z))
    
    # Count points inside the intersection
    in_intersection = 0
    for point in points:
        if is_in_sphere(point) and is_in_cylinder(point):
            in_intersection += 1
    
    # Calculate volume
    volume_box = (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
    volume_intersection = (in_intersection / num_points) * volume_box
    
    # Estimate uncertainty
    p = in_intersection / num_points  # Probability of a point being in intersection
    std_dev = np.sqrt(p * (1 - p) / num_points) * volume_box
    
    return volume_intersection, std_dev


# Run Monte Carlo simulation
num_simulations = 10
results = []
n_points = 1000000  # Using 1 million points for good precision

for _ in range(num_simulations):
    volume, error = monte_carlo_volume_estimation(n_points)
    results.append(volume)

# Calculate final results
mean_volume = np.mean(results)
std_error = np.std(results, ddof=1) / np.sqrt(num_simulations)
total_error = np.sqrt(std_error**2 + error**2)  # Combine both error sources

print(f"Estimated volume of sphere-cylinder intersection: {mean_volume:.6f} ¡À {total_error:.6f}")

