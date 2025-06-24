import cadquery as cq

# CONSTANTES (similar a Blender)
FUS_RIB_A_Y = -3.0
FUS_RIB_B_Y = 5.75
FUS_RIB_C_Y = 6.0

FUS_RIB_A_X = 8
FUS_RIB_A_Z = 4

FUS_RIB_B_INSET = 1.0
FUS_RIB_C_INSET = 0.25

REACTOR_THICK = 1.0

DRIVE_RAD = 3.85
DRIVE_THICK = 0.6
DRIVE_Y = -2.0

# FUNCIONES DE PARTES

def create_fuselage():
    # Rib A - caja escalada y posicionada
    rib_a = cq.Workplane("XY").box(FUS_RIB_A_X * 2, FUS_RIB_A_Z * 2, 1).translate((0, FUS_RIB_A_Y, 0))

    # Rib B - caja más pequeña y más arriba
    rib_b_x = FUS_RIB_A_X - FUS_RIB_B_INSET
    rib_b_z = FUS_RIB_A_Z - FUS_RIB_B_INSET
    rib_b = cq.Workplane("XY").box(rib_b_x * 2, rib_b_z * 2, 1).translate((0, FUS_RIB_B_Y, 0))

    # Rib C - caja aún más pequeña y más arriba
    rib_c_x = rib_b_x - FUS_RIB_C_INSET
    rib_c_z = rib_b_z - FUS_RIB_C_INSET
    rib_c = cq.Workplane("XY").box(rib_c_x * 2, rib_c_z * 2, 1).translate((0, FUS_RIB_C_Y, 0))

    return rib_a.union(rib_b).union(rib_c)

def create_reactor():
    # Reactor como cono truncado (frustum) - en CadQuery usamos cylinder con dos radios diferentes
    reactor = cq.Workplane("XY").cone(
        height=REACTOR_THICK,
        radius1=DRIVE_RAD,
        radius2=DRIVE_RAD - DRIVE_THICK
    ).translate((0, FUS_RIB_A_Y + 1.0, 0))
    return reactor

def add_thrusters():
    # Dos conos pequeños a los lados
    thruster1 = cq.Workplane("XY").cone(height=1.2, radius1=0.4, radius2=0.2).translate((2.0, DRIVE_Y, 0))
    thruster2 = cq.Workplane("XY").cone(height=1.2, radius1=0.4, radius2=0.2).translate((-2.0, DRIVE_Y, 0))
    return thruster1.union(thruster2)

def add_sensors():
    # Dos esferas pequeñas a los lados y un poco arriba
    sensor1 = cq.Workplane("XY").sphere(0.3).translate((1.5, FUS_RIB_B_Y + 0.5, 1.0))
    sensor2 = cq.Workplane("XY").sphere(0.3).translate((-1.5, FUS_RIB_B_Y + 0.5, 1.0))
    return sensor1.union(sensor2)

def add_shields():
    # Cubo escalado y posicionado para escudos
    shield = cq.Workplane("XY").box(5, 0.4, 3).translate((0, FUS_RIB_B_Y + 1.0, 0))
    return shield

# CREAR LA NAVE COMPLETA UNIDA

def create_spacecraft():
    fuselage = create_fuselage()
    reactor = create_reactor()
    thrusters = add_thrusters()
    sensors = add_sensors()
    shields = add_shields()

    # Unión de todas las partes en un solo sólido
    ship = fuselage.union(reactor).union(thrusters).union(sensors).union(shields)
    return ship

# MAIN
if __name__ == "__main__":
    ship = create_spacecraft()
    # Para visualizar en CQ-editor o exportar
    show_object(ship)  # CQ-editor muestra el objeto
    # Para exportar a STEP:
    # ship.val().exportStep("spaceship.step")
