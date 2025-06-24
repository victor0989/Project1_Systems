import bpy
import bmesh
from mathutils import Vector
from math import radians

def create_fuselage(bm):
    # Cuerpo central (caja alargada)
    bmesh.ops.create_cube(bm, size=2.0)
    # Escalado en x,z para hacerlo tipo fuselaje
    for v in bm.verts:
        v.co.x *= 4
        v.co.z *= 1.5
    # Extrusión frontal para la cabina
    front_faces = [f for f in bm.faces if all(v.co.y > 0.9 for v in f.verts)]
    if front_faces:
        face = front_faces[0]
        new_face = bmesh.ops.extrude_discrete_faces(bm, faces=[face])['faces'][0]
        bmesh.ops.translate(bm, vec=Vector((0, 1, 0.5)), verts=new_face.verts)

def create_thrusters(bm):
    thruster_radius = 0.3
    thruster_depth = 1.0
    for side in [-1, 1]:
        thruster_verts = bmesh.ops.create_cone(
            bm,
            cap_ends=True,
            segments=16,
            radius1=thruster_radius,
            radius2=thruster_radius * 0.6,
            depth=thruster_depth
        )['verts']
        bmesh.ops.translate(bm, vec=Vector((side * 3.5, -1.5, 0)), verts=thruster_verts)


def create_wings(bm):
    # Alas simples tipo cubos planos a los lados
    wing_size = Vector((2.5, 0.3, 1.0))
    for side in [-1, 1]:
        wing_verts = bmesh.ops.create_cube(bm, size=1.0)['verts']
        for v in wing_verts:
            v.co.x *= wing_size.x
            v.co.y *= wing_size.y
            v.co.z *= wing_size.z
        bmesh.ops.translate(bm, vec=Vector((side * 3.0, 0, 0)), verts=wing_verts)

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
