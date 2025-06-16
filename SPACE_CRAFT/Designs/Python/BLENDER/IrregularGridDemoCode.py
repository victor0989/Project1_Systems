import random
import cadquery as cq
from cadqueryhelper import irregular_grid
from cqindustry import Walkway
from cqterrain import tile as terrain_tile

#ig = irregular_grid(
#    height=3,
#    union_grid=False,
#    max_height=10
#)

ig = irregular_grid(
    length = 100,
    width = 50,
    col_size = 10,
    row_size = 10,
    max_columns = 1,
    max_rows = 1,
    union_grid=False,
    seed="test3",
    fill_cells = [(0,0,4,3), (4,0,2,4), (6,0,4,1)],
)

#show_object(ig)

i_grid = irregular_grid(
    length = 75,
    width = 50,
    height = 2,
    max_height = 10,
    col_size = 5,
    row_size = 5,
    union_grid=False,
    seed = "test",
    align_z =True,
    passes_count = 51,
    include_outline = True
)

#show_object(i_grid)


def custom_item(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length-1, width-1, height)
        .chamfer(0.5)
    )

i_grid_2 = irregular_grid(
    length = 150,
    width = 50,
    height = 2,
    max_height = 10,
    col_size = 5,
    row_size = 5,
    align_z = True,
    include_outline = True,
    union_grid = False,
    seed = "test",
    make_item = custom_item,
    max_columns = 5
)

show_object(i_grid_2.translate((0,-100,0)))


i_grid_4_sky_scapers = irregular_grid(
    length = 100,
    width = 100,
    height = 2,
    col_size = 10,
    row_size = 5,
    max_columns = 4,
    max_rows = 4,
    max_height=50,
    align_z = True,
    include_outline = True,
    union_grid = False,
    passes_count = 160,
    seed = "purple",
    make_item = custom_item
)

show_object(i_grid_4_sky_scapers)


tile_styles = [
    #terrain_tile.plain,
    #terrain_tile.chamfer_frame,
    terrain_tile.rivet,
    #terrain_tile.slot
]
tile_styles_count = len(tile_styles)

def custom_tile(length, width, height):
    #tile_style = random.randrange(0,tile_styles_count)
    #tile = tile_styles[tile_style](length, width, height)
    tile = terrain_tile.rivet(length, width, height)
    return tile

bp = Walkway()
bp.length = 75
bp.width = 50
bp.height = 6
bp.walkway_chamfer = 3

bp.render_slots = 'irregular'
bp.tile_height = 4
bp.tile_max_height = 4
bp.tile_seed = 'or'
bp.make_tile_method = custom_tile
bp.tile_max_columns = 5
bp.tile_max_rows = 5

bp.render_tabs = True
bp.tab_chamfer = 4.5
bp.tab_height = 2
bp.tab_length = 5

bp.render_rails = True
bp.rail_width = 4
bp.rail_height = 2
bp.rail_chamfer = 1.9

bp.render_rail_slots = False

bp.make()
walkway_small = bp.build()

show_object(walkway_small.translate((0,-160,0)))