# Como trimesh no tiene un método directo para crear toroides,
# lo reemplazamos por una malla generada manualmente.

def create_torus(R=0.6, r=0.12, segments=64, rings=32):
    """
    Crea un toroide en formato trimesh.
    R = radio mayor
    r = radio menor
    """
    vertices = []
    faces = []
    for i in range(segments):
        theta = 2 * np.pi * i / segments
        for j in range(rings):
            phi = 2 * np.pi * j / rings
            x = (R + r * np.cos(phi)) * np.cos(theta)
            y = (R + r * np.cos(phi)) * np.sin(theta)
            z = r * np.sin(phi)
            vertices.append([x, y, z])
    vertices = np.array(vertices)

    def index(i, j):
        return i * rings + j

    for i in range(segments):
        for j in range(rings):
            ni = (i + 1) % segments
            nj = (j + 1) % rings
            faces.append([index(i, j), index(ni, j), index(ni, nj)])
            faces.append([index(i, j), index(ni, nj), index(i, nj)])
    faces = np.array(faces)

    return trimesh.Trimesh(vertices=vertices, faces=faces)

# Crear las piezas de nuevo con toroides personalizados
cone = trimesh.creation.cone(radius=0.75, height=1.2, sections=128)

torus = create_torus(R=0.6, r=0.12)
torus.apply_translation([0, 0, 1.2])

solenoid = trimesh.creation.cylinder(radius=0.08, height=0.8, sections=64)
solenoid.apply_translation([0, 0, 1.2])

coils = []
for angle_deg in range(0, 360, 30):
    angle_rad = np.radians(angle_deg)
    x = 0.6 * np.cos(angle_rad)
    y = 0.6 * np.sin(angle_rad)
    coil = create_torus(R=0.05, r=0.015)
    coil.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2, [1, 0, 0]))
    coil.apply_translation([x, y, 1.2])
    coils.append(coil)

injector = trimesh.creation.cylinder(radius=0.02, height=0.2, sections=32)
injector.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2, [0, 1, 0]))
injector.apply_translation([0.75, 0, 1.3])

box = trimesh.creation.box(extents=[0.1, 0.05, 0.05])
box.apply_translation([-0.4, 0, 1.35])

full_model = trimesh.util.concatenate([
    cone, torus, solenoid, injector, box, *coils
])

# Exportar como archivo GLB
full_model.export('/mnt/data/tokamak_merlin_hybrid.glb')

# Devolver información del modelo
full_model.bounds, len(full_model.faces), len(full_model.vertices)
