import bpy
import bmesh
from mathutils import Vector
from math import radians

def sharpen_nose(bm):
    bm.faces.ensure_lookup_table()
    front_faces = [f for f in bm.faces if all(v.co.y > 0.9 for v in f.verts)]
    if not front_faces:
        return
    face = front_faces[0]
    center = face.calc_center_bounds()
    
    # Crear un vértice en la punta frontal
    nose_tip = bm.verts.new((center.x, center.y + 1.5, center.z))
    
    # Crear caras triangulares hacia la punta
    for loop in face.loops:
        v1 = loop.vert
        v2 = loop.link_loop_next.vert
        bm.faces.new((v1, v2, nose_tip))
    
    # Eliminar la cara frontal original
    bm.faces.remove(face)

def create_fuselage(bm):
    bmesh.ops.create_cube(bm, size=2.0)
    for v in bm.verts:
        v.co.x *= 4
        v.co.z *= 1.5
    sharpen_nose(bm)

def create_thrusters(bm):
    thruster_radius = 0.3
    thruster_depth = 1.2
    for side in [-1, 1]:
        thruster_verts = bmesh.ops.create_cone(
            bm,
            cap_ends=True,
            segments=16,
            radius1=thruster_radius * 0.8,
            radius2=0.05,  # Punta afilada
            depth=thruster_depth
        )['verts']
        bmesh.ops.translate(bm, vec=Vector((side * 3.5, -2.0, 0)), verts=thruster_verts)

def create_wings(bm):
    wing_size = Vector((2.5, 0.2, 0.8))
    for side in [-1, 1]:
        wing_verts = bmesh.ops.create_cube(bm, size=1.0)['verts']
        for v in wing_verts:
            v.co.x *= wing_size.x
            v.co.y *= wing_size.y
            v.co.z *= wing_size.z
            v.co.y += (v.co.x * 0.2)  # Inclinación hacia atrás
        bmesh.ops.translate(bm, vec=Vector((side * 3.0, 0.3, 0)), verts=wing_verts)

def main():
    mesh = bpy.data.meshes.new("FighterMesh")
    obj = bpy.data.objects.new("FighterShip", mesh)
    bpy.context.collection.objects.link(obj)

    bm = bmesh.new()
    create_fuselage(bm)
    create_thrusters(bm)
    create_wings(bm)
    bm.to_mesh(mesh)
    bm.free()

    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    bpy.ops.object.shade_smooth()

if __name__ == "__main__":
    main()
