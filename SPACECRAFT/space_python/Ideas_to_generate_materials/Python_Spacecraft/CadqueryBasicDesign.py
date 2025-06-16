import cadquery as cq
from cadquery import exporters
from OCP.gp import gp_Trsf, gp_Mat


# 1. Fuselaje
def fuselaje(longitud=4000, diametro=800):
    fuselaje = (
        cq.Workplane("XY")
        .ellipse(diametro/2, diametro/4)
        .extrude(longitud)
        .edges().fillet(10)
    )
    panel_size = 200
    for x in range(0, longitud, panel_size):
        for y in range(-diametro//2, diametro//2, panel_size):
            fuselaje = fuselaje.faces(">Z").workplane(offset=x).rect(panel_size, panel_size).cutThruAll()
    return fuselaje

# 2. Motor VASIMR
def motor_vasimr(altura=600, diametro=300, num_bobinas=5):
    motor = cq.Workplane("XY").cylinder(altura, diametro/2)
    for i in range(num_bobinas):
        bobina = (
            cq.Workplane("XY")
            .cylinder(10, (diametro/2)*0.9)
            .translate((0, 0, i * altura/(num_bobinas-1)))
        )
        motor = motor.union(bobina)
    return motor

# 3. Propulsor de plasma
def propulsor(diametro=250, altura=500):
    base = cq.Workplane("XY").cylinder(altura * 0.7, diametro / 2)
    tobera = (
        cq.Workplane("XY")
        .circle(diametro / 2)
        .workplane(offset=altura * 0.3)
        .circle(diametro / 3)
        .loft()
        .translate((0, 0, altura * 0.7))
    )
    return base.union(tobera)

# 4. Cabina domo
def cabina(diametro=600):
    domo = cq.Workplane("XY").sphere(diametro/2)
    corte = cq.Workplane("XY").box(diametro, diametro, diametro/2).translate((0, 0, -diametro/4))
    return domo.cut(corte)

# 5. Aletas plegables
def aleta(longitud=800, ancho=300, grosor=10, angulo=30):
    base = cq.Workplane("XY").box(longitud, ancho, grosor)
    bisagra = cq.Workplane("XY").cylinder(grosor*3, grosor/2).translate((0, 0, grosor/2))
    return base.union(bisagra).rotate((0, 0, 0), (0, 1, 0), angulo)

# 6. Escotilla (no usada por ahora)
def escotilla(ancho=300, alto=200, profundidad=20):
    return cq.Workplane("XY").box(ancho, alto, profundidad)

# Ensamblaje principal
def ensamblaje_principal():
    fus = fuselaje()
    mot = motor_vasimr().translate((0, 0, 4000))
    prop = propulsor().translate((0, 0, 3500))
    domo = cabina().translate((0, 0, 4200))
    ala1 = aleta().translate((400, 0, 3000))
    ala2 = aleta().mirror("YZ").translate((-400, 0, 3000))
    return fus.union(mot).union(prop).union(domo).union(ala1).union(ala2)

if __name__ == "__main__":
    escala = 0.001  # escala para reducir tamaño (de mm a m)
    nave_wp = ensamblaje_principal()
    nave_shape = nave_wp.val()

    # Crear transformación de escala
    trsf = gp_Trsf()
    matriz_escala = gp_Mat(
        escala, 0, 0,
        0, escala, 0,
        0, 0, escala
    )
    trsf.HVectorialPart(matriz_escala)

    # Aplicar la transformación de escala
    nave_shape = nave_shape.Transformed(trsf)

    exporters.export(nave_shape, "nave.step")
    exporters.export(nave_shape, "nave.stl")
    exporters.export(nave_shape, "nave.brep")

    print("Exportación completada: nave.step, nave.stl, nave.brep")



