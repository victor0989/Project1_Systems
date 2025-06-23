import cadquery as cq
from cqindustry.can import CanTower

bp_can_tower = CanTower()
bp_can_tower.render_can = False
bp_can_tower.can_height = 122
bp_can_tower.can_diameter = 66
bp_can_tower.cut_padding = .5
bp_can_tower.ring_width = 4.5
bp_can_tower.platform_height = 20
bp_can_tower.platform_ladder_extends = 10
bp_can_tower.make()
can_tower = bp_can_tower.build()

show_object(can_tower.translate((0,0,0)))

import cadquery as cq
from cqindustry import ChipTower

bp_tower = ChipTower()
bp_tower.stories = 3
bp_tower.story_height = 75

bp_platform = bp_tower.bp_platform
bp_platform.render_floor = True

bp_tower.make()
tower_ex = bp_tower.build()

show_object(tower_ex)

import cadquery as cq
from cqindustry.container import Container

bp_container = Container()
bp_container.bp_hinge.rotate_deg = -90

bp_container.make()

result = bp_container.build()
show_object(result)

import cadquery as cq
from cqindustry.dome import Dome, greeble

#init greebles
vent_bp = greeble.VentHexagon()
door_bp = greeble.DoorHexagon()
door_bp.hinge_x_translate = -4.5

window_pen_bp = greeble.WindowFrame()
window_pen_bp.type="pentagon"
window_pen_bp.margin=.1
window_pen_bp.render_pane = False

window_hex_bp = greeble.WindowFrame()
window_hex_bp.type="hexagon"
window_hex_bp.render_pane = False

# make dome
bp = Dome()

#center
bp.greebles_bp.append(window_pen_bp)

#ring 1
bp.greebles_bp.append(vent_bp)
bp.greebles_bp.append(window_hex_bp)
bp.greebles_bp.append(window_hex_bp)
bp.greebles_bp.append(window_hex_bp)
bp.greebles_bp.append(window_hex_bp)

#ring2
bp.greebles_bp.append(window_pen_bp)
bp.greebles_bp.append(window_hex_bp)
bp.greebles_bp.append(window_pen_bp)
bp.greebles_bp.append(window_hex_bp)
bp.greebles_bp.append(window_pen_bp)
bp.greebles_bp.append(door_bp)
bp.greebles_bp.append(window_pen_bp)
bp.greebles_bp.append(window_hex_bp)
bp.greebles_bp.append(window_pen_bp)
bp.greebles_bp.append(door_bp)

bp.render_greebles = True
bp.make()
dome = bp.build()

show_object(dome)

import cadquery as cq
from cqindustry.portal import Portal

bp_portal = Portal()
bp_portal.bp_frame.length = 150
bp_portal.bp_frame.width = 30
bp_portal.bp_frame.height = 150

bp_portal.render_base = False
bp_portal.render_hinges = True
bp_portal.bp_ramp.width = 10
bp_portal.make()


result_open = bp_portal.build()
show_object(result_open)

import cadquery as cq
from cqspoolterrain import PowerStation, SpoolCladdingGreebled

bp_power = PowerStation()
bp_power.bp_cladding = SpoolCladdingGreebled()
bp_power.bp_cladding.seed="morePower!"
bp_power.make()
power = bp_power.build()
#show_object(power)
cq.exporters.export(power,f"stl/powerStation_seed_{bp_power.bp_cladding.seed}.stl")