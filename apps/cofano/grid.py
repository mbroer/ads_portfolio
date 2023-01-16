from settings import *
from vpython import *
import vpy

grid = None

LENGTH = CONTAINER_OFFSET.x
HEIGHT = CONTAINER_OFFSET.y
WIDTH  = CONTAINER_OFFSET.z

GRID_FRAME_THICKNESS = 2

X_COLOR = color.red
Y_COLOR = color.blue
Z_COLOR = color.green

grid_scaf_visible = False
grid_axis_visible = False
grid_xyz_visible = False

def get_grid():
    global grid
    return grid

def grid_ui(_scene):
    _scene.append_to_title('<h4>Grid settings</h4>')

    checkbox(bind=grid_toggle, pos=_scene.title_anchor, text='Show grid', checked=grid_scaf_visible)
    checkbox(bind=grid_axis_toggle, pos=_scene.title_anchor, text='Show axis', checked=grid_axis_visible)
    _scene.append_to_title('<br>')

    checkbox(bind=grid_xyz_toggle, pos=_scene.title_anchor, text='Show empty XYZ', checked=grid_xyz_visible)

    _scene.append_to_title('<br>')
    checkbox(bind=None, pos=_scene.title_anchor, text='Grid bound coords', checked=False)
    checkbox(bind=None, pos=_scene.title_anchor, text='Toggle 2D/3D', checked=False)

    _scene.append_to_title('<hr>')


def grid_toggle(evt):
    global grid_scaf_visible
    grid_scaf_visible = evt.checked

    if grid is not None:
        if not hasattr(grid, 'visualization_scaffolding'):
            grid.visualize_grid()

        grid.visualization_scaffolding.visible = grid_scaf_visible

def grid_axis_toggle(evt):
    global grid_axis_visible
    grid_axis_visible = evt.checked

    if grid is not None:
        grid.visualization_axis.visible = grid_axis_visible

def grid_xyz_toggle(evt):
    global grid_xyz_visible
    grid_xyz_visible = evt.checked

    if grid is not None:
        if not hasattr(grid, 'visualization_grid_spot_coords'):
            grid.visualize_grid_spot_coords()

        for x in grid.visualization_grid_spot_coords:
            x.visible = grid_xyz_visible

class Grid:

    def __init__(self, boats, rows, columns, stacks):
        global grid
        global grid_scaf_visible
        global grid_xyz_visible
        grid = self

        self.rows = rows
        self.columns = columns
        self.stacks = stacks

        self.matrix = [[[0 for _ in range(stacks)] for _ in range(columns)] for _ in range(rows)] #grid[x][y] = [vertical stack]
       
        self.line_x = 0-(LENGTH/2)
        self.line_y = 0-(WIDTH/2)

        self.total_length = LENGTH*columns
        self.total_width  = WIDTH*rows
        self.total_height = HEIGHT*stacks

        self.ground = box(pos=scene.center - vector(0,5,0), length=self.total_length*10, height=5, width=self.total_width*10, color=vector(1,1,1) )

        self.visualize_x_y_z()
        if grid_scaf_visible:
            self.visualize_grid()

        if grid_xyz_visible:
            self.visualize_grid_spot_coords()

    def visualize_x_y_z(self):

        font_size_l = int(self.total_length / 6) 
        font_size_w = int(self.total_width / 6) 
        font_size_h = int(self.total_height / 6) 

        shaft_width_l = font_size_l*.1
        shaft_width_w = font_size_w*.1
        shaft_width_h = font_size_h*.1

        x = text(pos=scene.center + vector(self.line_x + self.total_length/2, 0, WIDTH/2 + self.line_y + self.total_width + font_size_l),  visible=False, text="X", color=X_COLOR, billboard=False, emissive=True, height=font_size_l, depth=1, align='center')
        y = text(pos=scene.center + vector((((LENGTH/1.5)*-1)), 0, (self.line_y + self.total_width/2) + font_size_w/2  ),                  visible=False, text="Y", color=Y_COLOR, billboard=False, emissive=True, height=font_size_w, depth=1, align='right')
        z = text(pos=scene.center + vector(y.pos.x - font_size_w/2.5, self.total_height/2 - font_size_h/2, x.pos.z - font_size_l/2 ),      visible=False, text="Z", color=Z_COLOR, billboard=False, emissive=True, height=font_size_h, depth=1, align='center')

        x.rotate(angle=pi/-2)
        y.rotate(angle=pi/-2)

        #setting visibility here causes freeze
        x_arrow1 = arrow(pos=scene.center + x.pos + vector(font_size_l/ 2, shaft_width_l/-2, font_size_l/-2),      axis=vector(5,0,0),     length=( self.total_length / 2) - font_size_l / 2 , shaftwidth=shaft_width_l, color=X_COLOR)
        x_arrow2 = arrow(pos=scene.center + x.pos + vector(font_size_l/-2, shaft_width_l/-2 ,font_size_l/-2),      axis=vector(-5,0,0),    length=( self.total_length / 2) - font_size_l / 2 , shaftwidth=shaft_width_l, color=X_COLOR)

        y_arrow1 = arrow(pos=scene.center + y.pos + vector(font_size_w/-2.5, shaft_width_w/-2, font_size_w*-1),    axis=vector(0,0,-5),    length=( self.total_width / 2) - font_size_w / 2 , shaftwidth=shaft_width_w, color=Y_COLOR)
        y_arrow2 = arrow(pos=scene.center + y.pos + vector(font_size_w/-2.5, shaft_width_w/-2, font_size_w*.05),   axis=vector(0,0,5),     length=( self.total_width / 2) - font_size_w / 2 , shaftwidth=shaft_width_w, color=Y_COLOR)

        z_arrow1 = arrow(pos=scene.center + z.pos + vector(0,font_size_h,0),       axis=vector(0,5,0),   length=(self.total_height / 2) - font_size_h / 2 , shaftwidth=shaft_width_h, color=Z_COLOR)
        z_arrow2 = arrow(pos=scene.center + z.pos - vector(0,font_size_h*.05,0),   axis=vector(0,-5, 0), length=(self.total_height / 2) - font_size_h / 2 , shaftwidth=shaft_width_h, color=Z_COLOR)

        self.visualization_axis = compound([x,y,z,x_arrow1, x_arrow2, y_arrow1, y_arrow2, z_arrow1, z_arrow2],visible=grid_axis_visible) #cant use compound on curves >.>
        self.visualization_axis.opacity = 0.45

    def visualize_grid_spot_coords(self):

        self.visualization_grid_spot_coords = list()

        fontsize = int(WIDTH / 6)
        heightoffset = HEIGHT/2 - fontsize/2

        for z in range(self.stacks):
            for y in range(self.rows):
                for x in range(self.columns):
                    self.visualization_grid_spot_coords.append(
                        text(pos=scene.center + vector((x * LENGTH), (heightoffset + (z * HEIGHT)), (y * WIDTH)),  visible=True, text=(str(y)+","+str(x)+","+str(z)), color=vector(1,1,1), billboard=True, emissive=True, height=fontsize, depth=1, align='center')
                    )

    def visualize_grid(self):
        self.visualization_scaffolding = list()

        z = 0
        for i in range(self.stacks+1):

            y = 0-(WIDTH/2)
            x = 0-(LENGTH/2)

            for i in range(self.rows+1):
                # x axis
                self.visualization_scaffolding.append( 
                    box( pos=(scene.center + vector(self.line_x + self.total_length/2, z, y)), length=self.total_length, height=GRID_FRAME_THICKNESS, width=GRID_FRAME_THICKNESS, color=X_COLOR, visible=False)
                )

                y += WIDTH
            for i in range(self.columns+1):
                # y axis
                self.visualization_scaffolding.append( 
                    box( pos=(scene.center + vector(x, z, self.line_y + self.total_width/2 )), length=GRID_FRAME_THICKNESS, height=GRID_FRAME_THICKNESS,  width=self.total_width, color=Y_COLOR, visible=False)
                )

                for j in range(self.rows+1):
                    # up axis
                    self.visualization_scaffolding.append( 
                        box( pos=(scene.center + vector(x, self.total_height/2, self.line_y + (WIDTH*j) )), length=GRID_FRAME_THICKNESS, height=self.total_height, width=GRID_FRAME_THICKNESS, color=Z_COLOR, visible=False)
                    )

                x += LENGTH

            z += HEIGHT

        self.visualization_scaffolding = compound(self.visualization_scaffolding, visible=grid_scaf_visible) #cant use compound on curves >.>
        self.visualization_scaffolding.opacity = 0.65

    def remove(self):

        self.matrix = None
        del self.matrix
        self.visualization_axis.visible = False
        del self.visualization_axis

        if hasattr(self, 'visualization_scaffolding'):
            self.visualization_scaffolding.visible = False
            del self.visualization_scaffolding

        if hasattr(self, 'visualization_grid_spot_coords'):
            for x in self.visualization_grid_spot_coords:
                x.visible = False
            del self.visualization_grid_spot_coords

        self.ground.visible = False
        del self.ground
        del self

    def grid_to_coordinates(self, row, column, stack):
        return scene.center + vpy.vector_multiply(vector(column, stack, row), CONTAINER_OFFSET) + vector(0, CONTAINER_HEIGHT/2, 0)