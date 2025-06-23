import bpy

# Limpia la escena
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Importa el modelo GLB generado
bpy.ops.import_scene.gltf(filepath="//tokamak_merlin_hybrid.glb")

# Configura motor de render
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.device = 'GPU'

# === FUNCIONES DE MATERIALES ===
def crear_material(nombre, base_color, metalicidad, rugosidad):
    mat = bpy.data.materials.new(name=nombre)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = base_color
    bsdf.inputs["Metallic"].default_value = metalicidad
    bsdf.inputs["Roughness"].default_value = rugosidad
    return mat

# Material Inconel (oscuro, metálico, rugoso)
mat_inconel = crear_material("Inconel", (0.1, 0.1, 0.12, 1), metalicidad=1.0, rugosidad=0.3)

# Material Titanio (plateado claro, pulido)
mat_titanio = crear_material("Titanium", (0.7, 0.7, 0.75, 1), metalicidad=1.0, rugosidad=0.15)

# Material Cerámica (blanco hueso, no metálico)
mat_ceramica = crear_material("Ceramic", (0.95, 0.95, 0.9, 1), metalicidad=0.0, rugosidad=0.5)

# === ASIGNACIÓN INTELIGENTE SEGÚN NOMBRE OBJETO ===
for obj in bpy.context.scene.objects:
    if obj.type == 'MESH':
        obj.select_set(True)
        obj.data.materials.clear()
        if "cone" in obj.name.lower() or "nozzle" in obj.name.lower():
            obj.data.materials.append(mat_titanio)
        elif "coil" in obj.name.lower() or "torus" in obj.name.lower():
            obj.data.materials.append(mat_inconel)
        elif "solenoid" in obj.name.lower() or "injector" in obj.name.lower():
            obj.data.materials.append(mat_inconel)
        elif "box" in obj.name.lower() or "shield" in obj.name.lower():
            obj.data.materials.append(mat_ceramica)
        else:
            obj.data.materials.append(mat_titanio)

# === CÁMARA AUTOMÁTICA Y LUZ ===
bpy.ops.object.light_add(type='AREA', location=(2, -2, 3))
bpy.data.lights['Area'].energy = 500

bpy.ops.object.camera_add(location=(2.5, -2.5, 2), rotation=(1.1, 0, 0.78))
bpy.context.scene.camera = bpy.context.object

print(" Materiales aplicados y escena preparada.")
