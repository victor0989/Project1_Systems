import bpy
import bmesh
import math
from mathutils import Vector, Matrix
from random import random, uniform, seed, randrange, randint

# Helpers
def reset_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)

def extrude_face(bm, face, distance):
    geom = bmesh.ops.extrude_face_region(bm, geom=[face])
    verts = [ele for ele in geom['geom'] if isinstance(ele, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, vec=face.normal * distance, verts=verts)
    new_faces = [ele for ele in geom['geom'] if isinstance(ele, bmesh.types.BMFace)]
    return new_faces[0] if new_faces else face

def scale_face(bm, face, sx, sy, sz):
    center = face.calc_center_bounds()
    mat = Matrix.Diagonal(Vector((sx, sy, sz))).to_4x4()
    for v in face.verts:
        v.co = mat @ (v.co - center) + center

def get_aspect_ratio(face):
    coords = [v.co for v in face.verts]
    if len(coords) < 2:
        return 1.0
    edge_lengths = [ (coords[i] - coords[(i+1)%len(coords)]).length for i in range(len(coords)) ]
    return max(edge_lengths) / min(edge_lengths)

def is_rear_face(face):
    return face.normal.x < -0.9

def generate_spaceship():
    seed()

    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)

    scale_vector = Vector((uniform(0.75, 2.0), uniform(0.75, 2.0), uniform(0.75, 2.0)))
    bmesh.ops.scale(bm, vec=scale_vector, verts=bm.verts)

    for face in bm.faces[:]:
        if abs(face.normal.x) > 0.5:
            length = uniform(0.3, 1.0)
            for _ in range(randrange(3, 6)):
                if random() > 0.1:
                    face = extrude_face(bm, face, length)
                    if random() > 0.5:
                        scale_face(bm, face, 1, uniform(0.8, 1.2), uniform(0.8, 1.2))

    # Convert BMesh to mesh
    me = bpy.data.meshes.new('Spaceship')
    bm.to_mesh(me)
    bm.free()

    obj = bpy.data.objects.new('Spaceship', me)
    bpy.context.collection.objects.link(obj)

    # Select object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Center it
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    obj.location = (0, 0, 0)

    return obj

def setup_camera(obj):
    # Create or move camera
    cam = bpy.data.objects.get('Camera')
    if not cam:
        cam_data = bpy.data.cameras.new('Camera')
        cam = bpy.data.objects.new('Camera', cam_data)
        bpy.context.collection.objects.link(cam)

    cam.location = (5, -5, 3)
    cam.rotation_euler = (math.radians(65), 0, math.radians(45))
    bpy.context.scene.camera = cam

    # Point camera to object
    constraint = cam.constraints.get('TrackTo') or cam.constraints.new(type='TRACK_TO')
    constraint.target = obj
    constraint.track_axis = 'TRACK_NEGATIVE_Z'
    constraint.up_axis = 'UP_Y'

def setup_lighting():
    # Add light
    light_data = bpy.data.lights.new(name="Light", type='SUN')
    light = bpy.data.objects.new(name="Light", object_data=light_data)
    bpy.context.collection.objects.link(light)
    light.location = (5, 5, 10)

def main():
    reset_scene()
    spaceship = generate_spaceship()
    setup_camera(spaceship)
    setup_lighting()

main()
