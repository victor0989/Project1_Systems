# Rocket Viewer Notebook
#from rocket_params import *
#from models.airframe import build_airframe
#from models.nose_cone import build_nose
#from models.motor_mount import build_motor_mount
#from models.avionics_bay import build_av_bay
#from models.fins import build_fins

from cadquery import exporters
from cadquery import Assembly

# Construcción del modelo
airframe = build_airframe()
nose = build_nose()
motor = build_motor_mount()
av_bay = build_av_bay()
fins = build_fins()

# Ensamblaje usando Assembly
rocket = Assembly()
rocket.add(airframe, name='airframe')
rocket.add(nose.translate((0, 0, AIRFRAME_LENGTH)), name='nose')
rocket.add(motor, name='motor')
rocket.add(av_bay.translate((0, 0, 200)), name='avionics')
rocket.add(fins, name='fins')

# Mostrar en Jupyter
# show(rocket)
