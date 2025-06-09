import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Constantes físicas simplificadas
G = 6.67430e-11  # m^3/kg/s^2
m_earth = 5.972e24  # kg
m_moon = 7.348e22  # kg
d = 384400e3  # distancia Tierra-Luna en metros

# Cálculo del punto L1
def f_L1(r):
    return G * m_earth / r**2 - G * m_moon / (d - r)**2 - (r * (m_earth + m_moon) * G / d**3)

r_L1 = fsolve(f_L1, d / 2)[0]  # Aproximación inicial: la mitad

print(f"Distancia de L1 desde la Tierra: {r_L1/1e3:.2f} km")

# Coordenadas de cuerpos
x_earth, x_moon = 0, d
x_L1 = r_L1

# Visualización del campo de potencial efectivo
x = np.linspace(-0.2*d, 1.2*d, 1000)
y = np.linspace(-0.5*d, 0.5*d, 1000)
X, Y = np.meshgrid(x, y)

# Distancias a Tierra y Luna
r1 = np.sqrt((X - x_earth)**2 + Y**2)
r2 = np.sqrt((X - x_moon)**2 + Y**2)

# Potencial efectivo (simplificado)
Omega = -G * m_earth / r1 - G * m_moon / r2
plt.figure(figsize=(10, 8))
plt.contourf(X/1e6, Y/1e6, Omega, levels=100, cmap='plasma')
plt.colorbar(label='Potencial efectivo (J/kg)')
plt.plot([x_earth/1e6, x_moon/1e6], [0, 0], 'wo', label='Tierra y Luna')
plt.plot(x_L1/1e6, 0, 'go', label='Punto L1')
plt.xlabel('x (millones de km)')
plt.ylabel('y (millones de km)')
plt.title('Campo de potencial efectivo en el sistema Tierra-Luna')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
