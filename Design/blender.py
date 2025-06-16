import bpy
import math

def clean_scene(): 
bpy.ops.object.select_all(action='SELECT') 
bpy.ops.object.delete(use_global=False)

def create_cylinder(name, radius=1, depth=2, location=(0, 0, 0)): 
bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, location=location) 
obj = bpy.context.active_object 
obj.name = name 
return obj

def create_dome(name, radius=1, location=(0, 0, 0)): 
bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=location) 
obj = bpy.context.active_object 
bpy.ops.object.mode_set(mode='EDIT') 
bpy.ops.mesh.select_all(action='DESELECT') 
bpy.ops.mesh.select_face_by_sides(number=4, type='GREATER') 
bpy.ops.mesh.delete(type='FACE') # Remove bottom half to create dome 
bpy.ops.object.mode_set(mode='OBJECT') 
obj.name = name 
return obj

def create_cube(name, size=(1, 1, 1), location=(0, 0, 0)): 
bpy.ops.mesh.primitive_cube_add(size=1, location=location) 
obj = bpy.context.active_object 
obj.scale = (size[0]/2, size[1]/2, size[2]/2) 
obj.name = name 
return obj

def create_walkway(length=3, width=1, height=0.2, location=(0, 0, 0)): 
return create_cube("Walkway", size=(length, width, height), location=location)

def create_engine_pack(radius=0.5, depth=1.5, location=(0, 0, 0)): 
return create_cylinder("IonEngine", radius=radius, depth=depth, location=location)

# --- SHIP ASSEMBLY ---

clean_scene()

# Main body (CanTower)
body = create_cylinder("Body", radius=0.66, depth=1.22, location=(0, 0, 0.61))

# Central tower (ChipTower)
tower = create_cube("Tower", size=(0.5, 0.5, 2.25), location=(0, 0, 2.1))

# Front dome (Dome)
dome = create_dome("Dome", radius=0.66, location=(0, 0, 3.3))

# Side containers
container_left = create_cube("ContainerLeft", size=(0.4, 0.4, 1), location=(-1.0, 0, 0.5))
container_right = create_cube("ContainerRight", size=(0.4, 0.4, 1), location=(1.0, 0, 0.5))

# Rear ion engines (PowerStation inspired)
engine_left = create_engine_pack(location=(-0.5, -1.5, 0.25))
engine_right = create_engine_pack(location=(0.5, -1.5, 0.25))

# Walkway as access ramp
walkway = create_walkway(length=1.5, width=0.5, height=0.1, location=(0, -1.8, 0.05))

# Modular city (urban structure)
def create_skyscraper_grid(rows=2, cols=2, spacing=1.2, height_range=(1, 3)): 
import random 
for i in range(rows): 
for j in range(cols): 
h = random.uniform(*height_range) 
x = i * spacing 
y = j * spacing 
create_cube("Building", size=(0.4, 0.4, h), location=(x, y, h/2 + 0.1))

create_skyscraper_grid(rows=3, cols=3, spacing=1.5, height_range=(0.5, 2.5))

print("Ship assembled in Blender
