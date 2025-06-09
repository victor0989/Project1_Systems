import matplotlib.pyplot as plt

def draw_propulsion_system():
    plt.figure(figsize=(10, 8))
    ax = plt.gca()
    ax.set_facecolor('#0a0a23')  # Fondo oscuro tipo blueprint
    plt.title("Futuristic Propulsion System Design", color='white', fontsize=16, fontweight='bold')

    # Desactivar ejes
    plt.axis('off')

    # Coordenadas y nombres de componentes (x,y)
    components = {
        "1. Plasma Injector (VASIMR Nozzle)": (0.2, 0.8),
        "2. Ionization Chamber": (0.4, 0.85),
        "3. Magnetic Containment Coils": (0.6, 0.9),
        "4. Gravity Manipulation Core": (0.5, 0.6),
        "5. Micro Black Hole Reactor": (0.5, 0.4),
        "6. Power Distribution Array": (0.3, 0.3),
        "7. Thermal Radiation Shields": (0.7, 0.3),
        "8. Navigation Control Unit": (0.2, 0.15),
        "9. Fusion Pre-Stabilizer": (0.6, 0.2),
        "10. Quantum Field Stabilizer": (0.8, 0.15),
    }

    # Dibujar nodos (círculos) y etiquetas
    for comp, (x, y) in components.items():
        ax.plot(x, y, 'o', markersize=15, color='cyan', alpha=0.8)
        ax.text(x, y-0.05, comp, fontsize=9, fontfamily='monospace', color='white',
                ha='center', va='top', wrap=True)

    # Dibujar líneas de conexión (solo un ejemplo conceptual)
    connections = [
        ("1. Plasma Injector (VASIMR Nozzle)", "2. Ionization Chamber"),
        ("2. Ionization Chamber", "3. Magnetic Containment Coils"),
        ("3. Magnetic Containment Coils", "4. Gravity Manipulation Core"),
        ("4. Gravity Manipulation Core", "5. Micro Black Hole Reactor"),
        ("5. Micro Black Hole Reactor", "6. Power Distribution Array"),
        ("5. Micro Black Hole Reactor", "7. Thermal Radiation Shields"),
        ("6. Power Distribution Array", "8. Navigation Control Unit"),
        ("7. Thermal Radiation Shields", "9. Fusion Pre-Stabilizer"),
        ("9. Fusion Pre-Stabilizer", "10. Quantum Field Stabilizer"),
    ]

    for c1, c2 in connections:
        x1, y1 = components[c1]
        x2, y2 = components[c2]
        ax.plot([x1, x2], [y1, y2], color='cyan', linestyle='--', alpha=0.6)

    # Guardar imagen
    plt.savefig("propulsion_system_design.png", dpi=300, bbox_inches='tight', facecolor='#0a0a23')
    #plt.show()

if __name__ == "__main__":
    draw_propulsion_system()
