import numpy as np
import matplotlib.pyplot as plt

# Parámetros del motor tipo Merlin 1D
motor = {
    'combustion_chamber_radius': 0.3,  # m
    'combustion_chamber_height': 0.5,  # m
    'nozzle_exit_radius': 0.8,  # m
    'nozzle_length': 1.2,  # m
    'injector_radius': 0.25,  # m
    'fuel': 'RP-1',
    'oxidizer': 'LOX'
}


# Dibujar perfil 2D simplificado del motor
def draw_merlin_profile(motor):
    fig, ax = plt.subplots()

    # Cámara de combustión
    chamber = plt.Rectangle((-motor['combustion_chamber_radius'], 0),
                            2 * motor['combustion_chamber_radius'],
                            motor['combustion_chamber_height'],
                            color='red', alpha=0.6, label='Combustion Chamber')

    # Inyector
    injector = plt.Circle((0, motor['combustion_chamber_height'] + 0.1),
                          motor['injector_radius'],
                          color='blue', alpha=0.6, label='Injector')

    # Tobera (simplificada como un cono)
    nozzle_x = [-motor['combustion_chamber_radius'],
                -motor['nozzle_exit_radius'],
                motor['nozzle_exit_radius'],
                motor['combustion_chamber_radius']]
    nozzle_y = [0,
                -motor['nozzle_length'],
                -motor['nozzle_length'],
                0]

    ax.add_patch(chamber)
    ax.add_patch(injector)
    ax.plot(nozzle_x, nozzle_y, color='gray', label='Nozzle')

    ax.set_aspect('equal')
    ax.set_title("Perfil 2D Simplificado - Motor Merlin 1D")
    ax.legend()
    plt.grid()
    plt.show()


draw_merlin_profile(motor)
