import bpy
import math

# Eliminar todos los objetos previos
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Parámetros ajustados en metros
major_r = 1.0
minor_r = 0.3
coil_th = 0.075
sol_th = 0.2
nozzle_len = 1.5
nozzle_exit = 0.8
tube_r = 0.05
shield_th = 1.1

# Crear el toroide principal (campo magnético del tokamak)
bpy.ops.mesh.primitive_torus_add(major_radius=major_r, minor_radius=minor_r, location=(0, 0, 0))
torus = bpy.context.object
torus.name = "Toroide_Tokamak"

# Crear solenoide central
bpy.ops.mesh.primitive_cylinder_add(radius=sol_th, depth=2*major_r, location=(0, 0, 0))
solenoid = bpy.context.object
solenoid.name = "Solenoide_Central"
solenoid.rotation_euler[0] = math.radians(90)

# Crear blindaje térmico exterior
bpy.ops.mesh.primitive_cylinder_add(radius=major_r + shield_th, depth=1.0, location=(0, 0, 0))
shield = bpy.context.object
shield.name = "Blindaje_Exterior"
shield.rotation_euler[0] = math.radians(90)

# Crear tobera de escape
bpy.ops.mesh.primitive_cone_add(radius1=nozzle_exit, radius2=0.1, depth=nozzle_len, location=(0, -major_r - 1.0, 0))
nozzle = bpy.context.object
nozzle.name = "Tobera"
nozzle.rotation_euler[0] = math.radians(90)

# Tubo de inyección de deuterio
bpy.ops.mesh.primitive_cylinder_add(radius=tube_r, depth=1.2, location=(major_r, 0, 0))
tube = bpy.context.object
tube.name = "Tubo_Deuterio"
tube.rotation_euler[1] = math.radians(90)

# Agrupar todos los elementos
bpy.ops.object.select_all(action='DESELECT')
for obj in [torus, solenoid, shield, nozzle, tube]:
    obj.select_set(True)
bpy.context.view_layer.objects.active = torus
bpy.ops.object.join()

# Renombrar el conjunto
bpy.context.object.name = "Motor_Tokamak_Hibrido"

print("Modelo generado exitosamente.")
