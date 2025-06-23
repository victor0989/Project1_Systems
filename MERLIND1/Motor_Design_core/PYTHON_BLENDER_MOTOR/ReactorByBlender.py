import bpy
import math

# Limpia escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Motor de render
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'

# === FUNCIONES DE MATERIALES PBR ===
def crear_material(nombre, base_color, metalicidad, rugosidad):
    mat = bpy.data.materials.new(name=nombre)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = base_color
    bsdf.inputs["Metallic"].default_value = metalicidad
    bsdf.inputs["Roughness"].default_value = rugosidad
    return mat

# Materiales realistas
mat_inconel = crear_material("Inconel", (0.1, 0.1, 0.12, 1), 1.0, 0.35)
mat_titanio = crear_material("Titanium", (0.7, 0.7, 0.75, 1), 1.0, 0.15)
mat_ceramica = crear_material("Ceramic", (0.95, 0.95, 0.9, 1), 0.0, 0.5)

# === GEOMETRÍA DEL MOTOR ===

# Tobera Merlin (invertida)
bpy.ops.mesh.primitive_cone_add(vertices=128, radius1=0.25, radius2=0.75, depth=1.2, location=(0,0,0))
tobera = bpy.context.object
tobera.rotation_euler[0] = math.pi
tobera.data.materials.append(mat_titanio)

# Toroide Tokamak
bpy.ops.mesh.primitive_torus_add(major_radius=0.6, minor_radius=0.12, location=(0, 0, 1.2))
tokamak = bpy.context.object
tokamak.data.materials.append(mat_inconel)

# Solenoide vertical
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.8, location=(0,0,1.2))
solenoide = bpy.context.object
solenoide.data.materials.append(mat_inconel)

# Bobinas toroidales alrededor
for angle in range(0, 360, 30):
    x = 0.6 * math.cos(math.radians(angle))
    y = 0.6 * math.sin(math.radians(angle))
    bpy.ops.mesh.primitive_torus_add(major_radius=0.05, minor_radius=0.015, location=(x,y,1.2), rotation=(math.pi/2,0,0))
    coil = bpy.context.object
    coil.data.materials.append(mat_inconel)

# Inyector de deuterio
bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.2, location=(0.75, 0, 1.3), rotation=(0, math.pi/2, 0))
injector = bpy.context.object
injector.data.materials.append(mat_inconel)

# Conductos de refrigeración (simétricos)
for angle in range(0, 360, 120):
    x = 0.55 * math.cos(math.radians(angle))
    y = 0.55 * math.sin(math.radians(angle))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.25, location=(x, y, 1.4), rotation=(0, math.pi/2, 0))
    pipe = bpy.context.object
    pipe.data.materials.append(mat_ceramica)

# Escudo térmico externo con hueco
bpy.ops.mesh.primitive_cylinder_add(radius=0.8, depth=0.3, location=(0, 0, 1.15))
outer = bpy.context.object
outer.data.materials.append(mat_ceramica)

bpy.ops.mesh.primitive_cylinder_add(radius=0.7, depth=0.3, location=(0, 0, 1.15))
inner = bpy.context.object

# Operación booleana para crear hueco
bool_mod = outer.modifiers.new(type="BOOLEAN", name="hollow")
bool_mod.object = inner
bool_mod.operation = 'DIFFERENCE'
bpy.context.view_layer.objects.active = outer
bpy.ops.object.modifier_apply(modifier=bool_mod.name)
bpy.data.objects.remove(inner)

# Caja electrónica de control
bpy.ops.mesh.primitive_cube_add(size=0.05, location=(-0.4, 0, 1.35))
box = bpy.context.object
box.data.materials.append(mat_ceramica)

# === LUZ Y CÁMARA ===
bpy.ops.object.light_add(type='AREA', location=(3, -2, 3))
bpy.data.lights['Area'].energy = 600

bpy.ops.object.camera_add(location=(2.5, -2.5, 2), rotation=(1.1, 0, 0.78))
bpy.context.scene.camera = bpy.context.object

print("✅ Motor Tokamak–Merlin creado con materiales realistas.")
