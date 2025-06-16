import svgwrite

dwg = svgwrite.Drawing('laser_design.svg', profile='tiny', size=("500px", "300px"))

# Fondo negro
dwg.add(dwg.rect(insert=(0, 0), size=("100%", "100%"), fill='black'))

# Láser
dwg.add(dwg.line(start=(50, 150), end=(200, 150), stroke='white', stroke_width=2))

# Beam Splitter
dwg.add(dwg.line(start=(200, 150), end=(250, 100), stroke='white', stroke_width=2))
dwg.add(dwg.line(start=(200, 150), end=(250, 200), stroke='white', stroke_width=2))

# Fotodetector
dwg.add(dwg.rect(insert=(250, 90), size=(20, 20), fill='white'))

# Espejo
dwg.add(dwg.line(start=(250, 200), end=(270, 200), stroke='white', stroke_width=2))

# Guardar SVG
dwg.save()
print("SVG guardado como 'laser_design.svg'")
