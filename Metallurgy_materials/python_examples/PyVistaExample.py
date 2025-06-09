import pyvista as pv

# Crear una malla simple: cubo
mesh = pv.Cube()

# Crear Plotter en modo off_screen (no abre ventana)
plotter = pv.Plotter(off_screen=True)

plotter.add_mesh(mesh, color='lightblue', show_edges=True)

# Guardar captura
filename = "prueba_offscreen.png"
plotter.screenshot(filename)

# Cerrar plotter
plotter.close()

print(f"Archivo guardado en: {filename}")
