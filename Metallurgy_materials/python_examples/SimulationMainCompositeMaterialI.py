# main.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Física y estructura del material
def simulate_material_resistance(temperature, pressure, radiation):
    """ Simula resistencia térmica y estructural de un material compuesto """
    # Coeficiente sintético representativo
    base_resistance = 1000  # unidad arbitraria
    degradation = 0.02 * temperature + 0.03 * pressure + 0.01 * radiation
    final_resistance = base_resistance - degradation
    return final_resistance

# Parámetros extremos como en entorno solar o cerca de agujero negro
temperature = 6000  # Kelvin
pressure = 5000     # atm
radiation = 2000    # W/m² (nivel elevado de rayos gamma o X)

resistance = simulate_material_resistance(temperature, pressure, radiation)

print(f"Material resistance under extreme conditions: {resistance:.2f} units")

# Visualización
params = ['Temperature', 'Pressure', 'Radiation']
values = [temperature, pressure, radiation]

plt.bar(params, values, color='orange')
plt.title('Input Conditions for Material Simulation')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
