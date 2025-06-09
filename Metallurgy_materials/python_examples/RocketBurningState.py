import matplotlib.pyplot as plt
import numpy as np

# Define time intervals and geometry parameters
time_intervals = [0, 1, 2, 3, 4]
radii = [1.0, 1.2, 1.4, 1.6, 1.8]  # Simulated regressed surfaces at intervals
theta = np.linspace(0, 2 * np.pi, 100)

# Plot successive contours of burning surface
fig, ax = plt.subplots(figsize=(6, 6))
for i, radius in enumerate(radii):
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    ax.plot(x, y, label=f'Time {time_intervals[i]}s')

# Add central cavity for the propellant grain
central_cavity_radius = 0.5
x_cavity = central_cavity_radius * np.cos(theta)
y_cavity = central_cavity_radius * np.sin(theta)
ax.fill(x_cavity, y_cavity, 'gray', alpha=0.5, label='Central cavity')

# Add slots (simplified as radial lines)
num_slots = 5
for i in range(num_slots):
    angle = i * 2 * np.pi / num_slots
    ax.plot([0, radii[-1] * np.cos(angle)], [0, radii[-1] * np.sin(angle)], 'k--', lw=0.8)

ax.set_aspect('equal')
ax.set_title('2D Burning Surface Contours of Propellant Grain')
ax.legend()
ax.axis('off')

plt.show()
