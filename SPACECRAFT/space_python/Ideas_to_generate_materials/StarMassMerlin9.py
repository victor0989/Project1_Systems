import numpy as np
import matplotlib.pyplot as plt

def V(r, M_star, epsilon):
    """
    Potential function V(r) for a star of mass M_star and parameter epsilon.
    V(r) = -M_star/r for r > M_star/epsilon
    V(r) = -epsilon for r <= M_star/epsilon
    """
    r_star = M_star / epsilon
    V_val = np.where(r > r_star, -M_star / r, -epsilon)
    return V_val

# Parámetros
epsilon = 0.01
M_star_values = [1.0, 0.5, 0.1, 0.05, 0.01]  # Secuencia de masas decrecientes

r = np.linspace(0.001, 1.0, 1000)  # Evitamos r=0 para evitar división por cero

plt.figure(figsize=(8,6))

for M_star in M_star_values:
    potential = V(r, M_star, epsilon)
    plt.plot(r, potential, label=f'M_star={M_star}')

plt.xlabel('r')
plt.ylabel('V(r)')
plt.title('Potential V(r) for decreasing M_star')
plt.legend()
plt.grid(True)
plt.show()
