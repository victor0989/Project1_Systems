import pyvista as pv
import numpy as np
import math

def preparar_malla(malla):
    """Aplica transformaciones para preparar la malla para operaciones booleanas."""
    malla_clean = malla.clean(tolerance=1e-6)
    malla_tri = malla_clean.triangulate()
    return malla_tri.extract_surface()

def generar_alabe(indice, num_alabes=9):
    alabe = pv.Box(bounds=(-0.1, 0.1, 0.0, 1.0, -0.05, 0.05))
    angulo = indice * (360 / num_alabes)
    alabe.rotate_z(angulo)
    radio = 0.5
    x = radio * math.cos(math.radians(angulo))
    y = radio * math.sin(math.radians(angulo))
    alabe.translate([x, y, 0])
    return preparar_malla(alabe)

cilindro = pv.Cylinder(radius=0.3, height=1.0, resolution=100)
conjunto = preparar_malla(cilindro)

for i in range(9):
    alabe = generar_alabe(i)
    try:
        conjunto = preparar_malla(conjunto).boolean_union(alabe)
        conjunto = preparar_malla(conjunto)
    except Exception as e:
        print(f"Error uniendo álabe {i + 1}: {e}")

if conjunto.n_points > 0:
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(conjunto, color="deepskyblue", show_edges=True)
    plotter.add_axes()
    plotter.show_grid()
    plotter.screenshot("nave_modelo.png")
    plotter.close()

else:
    print("La malla resultante está vacía. No se puede graficar.")


