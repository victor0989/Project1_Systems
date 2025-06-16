#Procedimientos modulares y paramétricos.
#Estructuras simétricas y asimétricas.
#Categorías visuales para motores, antenas, armas, sensores, etc.
#Preparación para animación o generación por lotes (frames de película).
#Materiales y modificadores listos para render.
import bpy
import bmesh
from math import radians
from mathutils import Vector, Matrix
from random import uniform, randint, randrange, seed, random

# Importa tus funciones personalizadas auxiliares aquí si las tienes
# (ej: extrude_face, scale_face, add_exhaust_to_face, etc.)
# Aquí asumimos que ya están definidas arriba como en tu código original.

def generate_spaceship(
    random_seed='',
    num_hull_segments_min=3,
    num_hull_segments_max=6,
    create_asymmetry_segments=True,
    num_asymmetry_segments_min=1,
    num_asymmetry_segments_max=5,
    create_face_detail=True,
    allow_horizontal_symmetry=True,
    allow_vertical_symmetry=False,
    apply_bevel_modifier=True,
    assign_materials=True
):
    if random_seed:
        seed(random_seed)

    # Crear geometría inicial
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    scale_vector = Vector((uniform(0.75, 2.0), uniform(0.75, 2.0), uniform(0.75, 2.0)))
    bmesh.ops.scale(bm, vec=scale_vector, verts=bm.verts)

    # Construcción del casco
    for face in bm.faces[:]:
        if abs(face.normal.x) > 0.5:
            hull_segment_length = uniform(0.3, 1)
            num_hull_segments = randrange(num_hull_segments_min, num_hull_segments_max)
            for i in range(num_hull_segments):
                is_last = i == num_hull_segments - 1
                if random() > 0.1:
                    face = extrude_face(bm, face, hull_segment_length)
                    if random() > 0.75:
                        face = extrude_face(bm, face, hull_segment_length * 0.25)

                    if random() > 0.5:
                        sy = uniform(1.2, 1.5)
                        sz = uniform(1.2, 1.5)
                        if is_last or random() > 0.5:
                            sy = 1 / sy
                            sz = 1 / sz
                        scale_face(bm, face, 1, sy, sz)

                    if random() > 0.5:
                        offset = uniform(0.1, 0.4) * scale_vector.z * hull_segment_length
                        vec = Vector((0, 0, offset if random() > 0.5 else -offset))
                        bmesh.ops.translate(bm, vec=vec, verts=face.verts)

                    if random() > 0.5:
                        angle = radians(5 if random() > 0.5 else -5)
                        bmesh.ops.rotate(bm, verts=face.verts, cent=(0, 0, 0),
                                         matrix=Matrix.Rotation(angle, 3, 'Y'))
                else:
                    rib_scale = uniform(0.75, 0.95)
                    face = ribbed_extrude_face(bm, face, hull_segment_length,
                                               randint(2, 4), rib_scale)

    # Segmentos asimétricos
    if create_asymmetry_segments:
        for face in bm.faces[:]:
            if get_aspect_ratio(face) > 4:
                continue
            if random() > 0.85:
                for i in range(randrange(num_asymmetry_segments_min, num_asymmetry_segments_max)):
                    face = extrude_face(bm, face, uniform(0.1, 0.4))
                    if random() > 0.25:
                        s = 1 / uniform(1.1, 1.5)
                        scale_face(bm, face, s, s, s)

    # Clasificación y detallado de caras
    if create_face_detail:
        engine_faces, grid_faces, antenna_faces = [], [], []
        weapon_faces, sphere_faces, disc_faces, cylinder_faces = [], [], [], []
        for face in bm.faces[:]:
            if get_aspect_ratio(face) > 3:
                continue
            val = random()
            if is_rear_face(face):
                if not engine_faces or val > 0.75:
                    engine_faces.append(face)
                elif val > 0.5:
                    cylinder_faces.append(face)
                elif val > 0.25:
                    grid_faces.append(face)
                else:
                    face.material_index = Material.hull_lights
            elif face.normal.x > 0.9:
                if face.normal.dot(face.calc_center_bounds()) > 0 and val > 0.7:
                    antenna_faces.append(face)
                    face.material_index = Material.hull_lights
                elif val > 0.4:
                    grid_faces.append(face)
            elif face.normal.z > 0.9:
                if face.normal.dot(face.calc_center_bounds()) > 0 and val > 0.7:
                    antenna_faces.append(face)
                elif val > 0.6:
                    grid_faces.append(face)
                elif val > 0.3:
                    cylinder_faces.append(face)
            elif face.normal.z < -0.9:
                if val > 0.75:
                    disc_faces.append(face)
                elif val > 0.5:
                    grid_faces.append(face)
                elif val > 0.25:
                    weapon_faces.append(face)
            elif abs(face.normal.y) > 0.9:
                if not weapon_faces or val > 0.75:
                    weapon_faces.append(face)
                elif val > 0.6:
                    grid_faces.append(face)
                elif val > 0.4:
                    sphere_faces.append(face)

        for f in engine_faces: add_exhaust_to_face(bm, f)
        for f in grid_faces: add_grid_to_face(bm, f)
        for f in antenna_faces: add_surface_antenna_to_face(bm, f)
        for f in weapon_faces: add_weapons_to_face(bm, f)
        for f in sphere_faces: add_sphere_to_face(bm, f)
        for f in disc_faces: add_disc_to_face(bm, f)
        for f in cylinder_faces: add_cylinders_to_face(bm, f)

    # Simetrías
    if allow_horizontal_symmetry and random() > 0.5:
        bmesh.ops.symmetrize(bm, input=bm.verts[:] + bm.edges[:] + bm.faces[:], direction="Y")
    if allow_vertical_symmetry and random() > 0.5:
        bmesh.ops.symmetrize(bm, input=bm.verts[:] + bm.edges[:] + bm.faces[:], direction="Z")

    # Finalizar geometría
    me = bpy.data.meshes.new('SpaceshipMesh')
    bm.to_mesh(me)
    bm.free()

    obj = bpy.data.objects.new('Spaceship', me)
    bpy.context.scene.collection.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Centrar y ubicar en origen
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    obj.location = (0, 0, 0)

    # Bevel para suavizado angular
    if apply_bevel_modifier:
        bevel_modifier = obj.modifiers.new('Bevel', 'BEVEL')
        bevel_modifier.width = uniform(5, 20)
        bevel_modifier.offset_type = 'PERCENT'
        bevel_modifier.segments = 2
        bevel_modifier.profile = 0.25
        bevel_modifier.limit_method = 'NONE'

    # Asignar materiales
    materials = create_materials()
    for mat in materials:
        me.materials.append(mat if assign_materials else bpy.data.materials.new(name="Material"))

    return obj

# Uso directo desde el editor de scripts de Blender
if __name__ == "__main__":
    generate_single_spaceship = True

    if generate_single_spaceship:
        reset_scene()
        obj = generate_spaceship()
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
                bpy.ops.view3d.view_selected(ctx)

