import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use("Qt5Agg")  # O prueba "Qt5Agg" si TkAgg no funciona

import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(8, 6))

# Cámara de combustión
chamber = patches.Rectangle((1, 2), 1.5, 2, linewidth=2, edgecolor='black', facecolor='orange', label='Combustion Chamber')
ax.add_patch(chamber)

# Tobera convergente-divergente (simplificada)
nozzle = patches.Polygon([[2.5, 2], [3, 1.5], [3.5, 1.5], [3.8, 2.5], [3.5, 3.5], [3, 3.5], [2.5, 4]],
                         closed=True, edgecolor='black', facecolor='gray', label='Nozzle')
ax.add_patch(nozzle)

# Tanques de propulsante
fuel_tank = patches.Circle((0.8, 3.5), 0.4, facecolor='blue', edgecolor='black', label='Fuel Tank')
oxidizer_tank = patches.Circle((0.8, 2.5), 0.4, facecolor='red', edgecolor='black', label='Oxidizer Tank')
ax.add_patch(fuel_tank)
ax.add_patch(oxidizer_tank)

# Etiquetas
ax.text(0.2, 3.5, "Fuel", fontsize=10)
ax.text(0.2, 2.5, "Oxidizer", fontsize=10)
ax.text(1.2, 3, "Chamber", fontsize=10)
ax.text(3.3, 2.2, "Nozzle", fontsize=10)

# Configuración de ejes
ax.set_xlim(0, 5)
ax.set_ylim(1, 5)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Rocket Engine Diagram (2D)")
plt.savefig("Nozzle.png")

