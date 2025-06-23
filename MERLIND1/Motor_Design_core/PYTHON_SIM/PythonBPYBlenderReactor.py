import bpy
import math

# Borrar todo
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Parámetros
scale = 1.0
tokamak_radius = 0.6 * scale
tokamak_thickness = 0.12 * scale
solenoid_height = 0.8 * scale
cone_height = 1.2 * scale

# Tobera (cono Merlin)
bpy.ops.mesh.primitive_cone_add(vertices=128, radius1=0.75*scale, radius2=0.25*scale, depth=cone_height, location=(0,0,0))

# Tokamak torus
bpy.ops.mesh.primitive_torus_add(
    major_radius=tokamak_radius,
    minor_radius=tokamak_thickness,
    location=(0, 0, cone_height)
)

# Solenoide central
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.08*scale,
    depth=solenoid_height,
    location=(0, 0, cone_height)
)

# Bobinas toroidales alrededor del toro
for angle in range(0, 360, 30):
    x = tokamak_radius * math.cos(math.radians(angle))
    y = tokamak_radius * math.sin(math.radians(angle))
    bpy.ops.mesh.primitive_torus_add(
        major_radius=0.05 * scale,
        minor_radius=0.015 * scale,
        location=(x, y, cone_height),
        rotation=(math.pi / 2, 0, 0)
    )

# Inyector de deuterio
bpy.ops.mesh.primitive_cylinder_add(
    radius=0.02*scale,
    depth=0.2*scale,
    location=(0.75*scale, 0, cone_height + 0.1),
    rotation=(0, math.pi/2, 0)
)

# Conductos de refrigeración
for angle in range(0, 360, 120):
    x = 0.55 * math.cos(math.radians(angle))
    y = 0.55 * math.sin(math.radians(angle))
    bpy.ops.mesh.primitive_cylinder_add(
        radius=0.01*scale,
        depth=0.25*scale,
        location=(x, y, cone_height + 0.2)
    )

# Sensores
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015*scale, location=(0.6*scale, 0, cone_height))
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.015*scale, location=(0, 0.6*scale, cone_height))

# Nodo de control
bpy.ops.mesh.primitive_cube_add(size=0.05*scale, location=(-0.4*scale, 0, cone_height + 0.15))
