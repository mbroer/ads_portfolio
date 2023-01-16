from vpython import *
import random
from copy import copy, deepcopy
import vpy
from time import sleep
import grid
from settings import *
from boat import boats

container_id = 0;
containers = list()
containers_stack = dict()

low_detail = False

#REGION UI

ui_container_dropdown = None
ui_container_validate_dropdown = None
scene = None
def container_ui(_scene):
    global ui_container_dropdown
    global ui_container_validate_dropdown
    global scene
    scene = _scene
    _scene.append_to_title('<h4>Container settings</h4>')

    wtext(text='Select container', pos=_scene.title_anchor)
    ui_container_dropdown = menu( bind=container_dropdown, pos=_scene.title_anchor, choices=[])
    _scene.append_to_title('<br>')

    wtext(text='Stack visibility', pos=_scene.title_anchor)
    slider(vertical=False, bind=container_hide_stack, pos=_scene.title_anchor, min=1, max=5, value=5, step=1, length=80)
    _scene.append_to_title('<br>')

    checkbox(bind=container_toggle_labels, pos=_scene.title_anchor, text='Container labels')

    _scene.append_to_title('<br>')

    button( bind=ui_new_container, text='New', pos=_scene.title_anchor )
    _scene.append_to_title(' ')
    button( bind=ui_delete_selected, text='Del selected', pos=_scene.title_anchor )
    _scene.append_to_title('<br>')
    wtext(text='Move selected ', pos=_scene.title_anchor)
    winput( bind=ui_movecontainer_input, text='x,y,z', pos=_scene.title_anchor )

    _scene.append_to_title('<br>')
    button( bind=validate_positions, text='Force validation', pos=_scene.title_anchor )
    ui_container_validate_dropdown = menu( bind=container_dropdown_aim_at, pos=_scene.title_anchor, choices=[])

    _scene.append_to_title('<hr>')

def container_dropdown_aim_at(id):
    scene.camera.axis = get_containers_by_id(ui_container_validate_dropdown.selected)[0].pos - scene.camera.pos

def ui_movecontainer_input(s):
    splits = s.text.split(',')
    row = int(splits[0])
    column = int(splits[1])
    stack = int(splits[2])

    if stack == -1:
        stack = None

    for cont in get_containers_by_id(ui_container_dropdown.selected):
        cont.move_to(row,column,None, True)

def ui_set_container_choices():
    global ui_container_dropdown
    ui_container_dropdown.choices = [str(i.id) for i in containers]

    if len(ui_container_dropdown.choices) > 0:
        ui_container_dropdown.selected = ui_container_dropdown.choices[0]

container_hide_stack_last = 5
def container_hide_stack(evt):

    global container_hide_stack_last
    if evt.value > container_hide_stack_last:
        stacks = range(0, evt.value)
        visible = True #up
    else:
        stacks = range(evt.value, 4)
        visible = False #down

    for i in stacks:
        if not i in containers_stack:
            continue

        for container in containers_stack.get(i):
            container.set_visibility(visible)

    container_hide_stack_last = evt.value

def container_toggle_labels(evt):
    for container in containers:

        if not container.visible:
            continue

        container._label.on = evt.checked
        container._label.visible = evt.checked

def container_dropdown(e):
    print(e.selected)

def ui_delete_selected():
    global ui_container_dropdown

    for cont in get_containers_by_id(ui_container_dropdown.selected):
        cont.remove()

    ui_set_container_choices()

def get_containers_by_id(id):
    return [c for c in containers if c.id==int(id)]

def ui_new_container():
    container_on_spot = get_container_at(-1, -1, 0)
    if isinstance(container_on_spot, Container):
        return

    cont = Container( boat=boats[0], position=vector(-1,-1, 0) )

    ui_set_container_choices()

list_nonvalid_containers = list()
def validate_positions():
    print("validate_positions")
    global ui_container_validate_dropdown
    global list_nonvalid_containers
    dropdown_choices = list()

    for container in list_nonvalid_containers:
        container.set_color(boats[container.boatid].color)

    for container in containers:
        if container_is_oob(container):
            list_nonvalid_containers.append(container)
            dropdown_choices.append(str(container.id))
            container.set_color(vector(0,0,0))
            continue

        if container.stack <= 0:
            continue

        c = get_container_at(container.row, container.column, container.stack-1)
        
        if not isinstance(c, Container):
            list_nonvalid_containers.append(container)
            dropdown_choices.append(str(container.id))
            container.set_color(vector(0,0,0))

    print(len(dropdown_choices))

    ui_container_validate_dropdown.choices = dropdown_choices

#ENDREGION UI

def post_init():
    ui_container_validate_dropdown.choices = []
    ui_set_container_choices()
    init_label_canmove()

def init_label_canmove():
    for container in containers:
        container._label.text += ( "\ncanmove: " + str(container.container_can_move()) )

def get_container_at(row, column, stack):
    if row <0 or stack <0 or column <0:
        return None
    try:
        return grid.grid.matrix[row][column][stack]
    except IndexError:
        return None

def get_container_stack_height_at(row, column):

    for stack in range(len(grid.grid.matrix[row][column])):
        if not isinstance(grid.grid.matrix[row][column][stack], Container):
            return stack

    return stack

def container_is_oob(container):
    if container.row < 0 or container.column <0 or container.stack <0:
        return True

    if container.row >= grid.grid.rows or container.column >= grid.grid.columns or container.stack >= grid.grid.stacks:
        return True

    return False
    #matrix = deepcopy(grid.grid.matrix)
    #try:
    #    grid.grid.matrix[container.row][container.column][container.stack] = container
    #    return False
    #except IndexError:
    #    return True

class Container:
    def __init__(self, boat, position, id=None):
        self.set_id(boat.id, id)
        self.set_position(position)
        self.visualize(boat.color)
        self.visualize_update()
        self.set_visibility(True)

        containers.append(self)
        containers_stack.setdefault(self.stack, []).append(self)

    def set_position(self, position):
        self.row = int(position.x)
        self.column = int(position.y)
        self.stack = int(position.z)    

        try:
            grid.grid.matrix[self.row][self.column][self.stack] = self
        except IndexError:
            print("oob, tried filling grid", self.row, self.column, self.stack)
        
        #print("pos", position)

        self.pos = grid.grid.grid_to_coordinates(self.row, self.column, self.stack)
        self.set_label()

    def set_id(self, boatid, id):
        global container_id
        self.id = container_id if id is None else id
        container_id += 1

        self.boatid = boatid

        self.textobj = text(visible=False, text=str(self.id), color=vector(1,1,1), billboard=False, emissive=True, height=10, axis=vector(20,0,1), depth=0.1, align='left')
        self.textobj.object = self
        

    def set_label(self):
        if not hasattr(self, '_label'):
            self._label = label(opacity=.7, space=30, height=16, border=4, visible=False)
            self._label.on = False

        self._label.text = f"id: {self.id}, ship id: {self.boatid}\nrow:{self.row}, col:{self.column}, stack:{self.stack}\nscore: ?\nvalid place: ?"

        #self.update_can_move_label()


    def visualize_update(self):

        pos = { "left": self.pos + vector(0,0,CONTAINER_WIDTH/2),
                "right": self.pos - vector(0,0,CONTAINER_WIDTH/2),
                "top": self.pos + vector(0,CONTAINER_HEIGHT/2,0),
                "bottom": self.pos - vector(0,CONTAINER_HEIGHT/2,0),
                "back": self.pos + vector(CONTAINER_LENGTH/2,0,0),
                "front": self.pos - vector(CONTAINER_LENGTH/2,0,0),
                "ld_box": self.pos
        }

        for key, texture in self.textures.items():
                texture.pos = pos[key]

        self.textobj.pos = self.textures["ld_box" if "ld_box" in self.textures else "left" ].bounding_box()[1]
        self._label.pos = self.pos + vector(0, CONTAINER_HEIGHT/4, 0)


    def visualize(self, color):

        if low_detail:
            self.textures = {"ld_box": box(length=CONTAINER_LENGTH, height=CONTAINER_HEIGHT, width= CONTAINER_WIDTH)}
        else:
            left    = box(visible=False, length=CONTAINER_LENGTH, height=CONTAINER_HEIGHT,  width=TEXTURE_DEPTH,                   texture={'file': 'textures/container/container_side.png', 'bumpmap':'textures/container/container_side_nm.png'} )
            top     = box(visible=False, length=CONTAINER_LENGTH, height=TEXTURE_DEPTH,     width=CONTAINER_WIDTH - TEXTURE_DEPTH, texture={'file': 'textures/container/container_top.png',  'bumpmap':'textures/container/container_top_nm.png'} )
            front   = box(visible=False, length=TEXTURE_DEPTH,    height=CONTAINER_HEIGHT,  width=CONTAINER_WIDTH - TEXTURE_DEPTH, texture={'file': 'textures/container/container_front.png','bumpmap':'textures/container/container_front_nm.png'} )
            back    = box(visible=False, length=TEXTURE_DEPTH,    height=CONTAINER_HEIGHT,  width=CONTAINER_WIDTH - TEXTURE_DEPTH, texture={'file': 'textures/container/container_back.png', 'bumpmap':'textures/container/container_back_nm.png'} )

            right   =   left.clone(visible=False)
            bottom  =    top.clone(visible=False)
            
            self.textures = {"left":   left, 
                             "right":  right,
                             "top":    top,
                             "bottom": bottom,
                             "front":  front,
                             "back":   back,
            }

        for key, texture in self.textures.items():
            texture.visible = False
            texture.shininess = 0
            texture.object = self

        self.set_color(color)


    def set_color(self, color):
        self.color = color

        for key, texture in self.textures.items():
            texture.color = color

    def set_visibility(self, bool):

        if not hasattr(self, 'visible'):
            self.visible = False

        if self.visible == bool:
            return

        self.visible = bool

        for key, texture in self.textures.items():
            texture.visible = bool

        self.textobj.visible = bool

        if self._label.on:
            self._label.visible = bool

        self.visible = bool

    def get_blocked_containers(self):
        containers = {
            "top": get_container_at(self.row, self.column, self.stack+1 ),
            "row_up": get_container_at(self.row-1, self.column, self.stack ),
            "row_down": get_container_at(self.row+1, self.column, self.stack ),
            "row_up_down": get_container_at(self.row-1, self.column, self.stack-1 ),
            "row_down_down": get_container_at(self.row+1, self.column, self.stack-1 )
        }

        return {k: v for k, v in containers.items() if isinstance(v, Container)}

    def container_can_move(self):
        containers = self.get_blocked_containers()
        return not ("top" in containers or "row_up" in containers and "row_down" in containers or "row_up_down" in containers and "row_down_down" in containers)

    def get_bounding_countainers(self):
        containers = [
            get_container_at(self.row, self.column, self.stack-1 ),
            get_container_at(self.row-1, self.column, self.stack ),
            get_container_at(self.row+1, self.column, self.stack )
        ]

        return [i for i in containers if isinstance(i, Container)]

    def update_can_move_label(self):
        text = self._label.text.rsplit('\n', 1)[0]
        self._label.text = text + "\ncan move: " + str(self.container_can_move())

    def move_to(self, row, column, stack=None, lerp=False, validate_move=True):
        global grid
        if stack is None:
            stack = get_container_stack_height_at(row, column)

        if validate_move:
            if vector(row, column, stack) == self.pos:
                return -1

            print("move", self.id, "to", row, column, stack)

            if vector(self.row, self.column, 0) == vector(row, column, 0):
                print(f"Container is already at row:{self.row}, col:{self.column}")
                #return

            if not self.container_can_move():
                print(f"Container with id {self.id} cannot be moved.")
                return -1

            container_on_spot = get_container_at(row, column, stack)
            if isinstance(container_on_spot, Container):
                print(f"Spot is already in use by container {container_on_spot.id}.")
                return -1

        list_containers = self.get_bounding_countainers()

        grid.grid.matrix[self.row][self.column][self.stack] = None

        if lerp:
            pos = self.pos
            goal = grid.grid.grid_to_coordinates(row, column, stack)
            diff = goal - pos

            #diff_2d = pos + vector(0,diff.y,0)
            #lift_height = diff.y + CONTAINER_HEIGHT * .2

            ### move up

            #self.pos += vector(0,lift_height,0)
            #self.visualize_update()

            pos = self.pos
            diff = goal - pos

            frames = int(vpy.vector_abs_dist(diff))
            frames = int(frames * .25)
            fps = 60
            animtime = frames / fps

            sleeptime = (animtime / frames) *.0025

            step = diff / frames

            for i in range(frames):
                pos += step

                self.pos = pos
                self.visualize_update()
                sleep(sleeptime)

            ### move down

        self.set_position(vector(row, column, stack))
        self.visualize_update()

        list_containers.extend(self.get_bounding_countainers())

        for c in list_containers:
            c.update_can_move_label()

        """ RECALCULATE ALL CANMOVES FROM MOVETO AND MOVEFROM TOP BOTTOM LEFT RIGHT """

    def remove(self):
        global grid
        global containers

        try:
            grid.grid.matrix[self.row][self.column][self.stack] = None
        except IndexError:
            print("grid oob")

        containers.remove(self)

        self.textobj.visible = False
        del self.textobj
        self._label.visible = False
        del self._label

        for key, texture in self.textures.items():
            texture.visible = False
            del texture

        