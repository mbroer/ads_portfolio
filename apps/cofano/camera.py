from vpython import *
import vpy
import container_animations as ca
import container as c
from grid import get_grid, LENGTH, HEIGHT, WIDTH
from time import sleep
import threading

scene = None

def keyInput(evt):
    s = evt.key

    left = vector(scene.camera.axis.x -1, scene.camera.axis.y, scene.camera.axis.z)
    scalar = scene.camera.axis*0.05

    if s == 'w':
        scene.camera.pos += scalar #scene.camera.pos + vector(1,0,0)
    elif s == 'a':
        scene.camera.pos -= vector(5,0,0)
    elif s == 's':
        scene.camera.pos -= scalar
    elif s == 'd':
        scene.camera.pos += vector(5,0,0)

    #print('['+s+']')
    #print( scalar, left, scene.camera.pos )
    #print( scene.camera.axis )

last_selected_container = None
def container_info(ev):
    global last_selected_container

    if ev.key != 'i':
        return

    obj = scene.mouse.pick

    if obj is None:
        return

    if isinstance(last_selected_container, c.Container):
        if hasattr(last_selected_container, '_label'):
            last_selected_container._label.on = False
            last_selected_container._label.visible = False

    if hasattr(obj, 'object'):
        container = obj.object
        #print('selected obj id', container.id)

        blocked_conts = container.get_blocked_containers()

        container._label.on = True
        container._label.visible = True
        last_selected_container = container

        thread = threading.Thread(target=ca.container_select_anim, args =([container])).start()

        for _c in blocked_conts.values():
            thread = threading.Thread(target = ca.container_blocked_anim, args = (container, _c))
            thread.start()

    else:
        if isinstance(ca.selected_container, c.Container):
            ca.selected_container._label.on = False
            ca.selected_container._label.visible = False

        ca.selected_container = None

drag_obj = None
is_holding_lmb = False
def set_holding_lmb():
    global drag_obj
    global is_holding_lmb
    is_holding_lmb = True
    drag_obj = scene.mouse.pick

def unset_holding_lmb():
    global is_holding_lmb
    global enable_select
    global drag_obj

    is_holding_lmb = False
    drag_obj = None

def drag_container_pickup():
    global is_holding_lmb

    if not is_holding_lmb or drag_obj is None:
        return

    if hasattr(drag_obj, 'object'):
        container = drag_obj.object
        container.pos = scene.mouse.pos
        container.visualize_update()

def drag_container_place():
    global drag_obj
    
    grid = get_grid()

    if drag_obj is None:
        return

    if not hasattr(drag_obj, 'object'):
        return

    container = drag_obj.object

    col = min(grid.columns-1, max(0, int(container.pos.x / LENGTH)))
    row = min(grid.rows-1, max(0, int(container.pos.z / WIDTH)))
    stack = min(grid.stacks-1, max(0, int(container.pos.y / HEIGHT)))

    container_on_spot = c.get_container_at(row, col, stack)

    if isinstance(container_on_spot, c.Container):
        print("cancel")
        container.set_position(vector(container.row, container.column, container.stack))
        container.visualize_update()
        return

    print(row, col, stack)
    res = container.move_to(row, col, stack, validate_move=False)

    if res == -1:
        container.set_position(vector(container.row, container.column, container.stack))
        container.visualize_update()



    #container.visualize_update()

    print(row, col, stack)


def main(_scene=None):
    global scene
    scene = _scene

    scene.bind("mouseup", drag_container_place )

    scene.bind('keydown', container_info)
    scene.bind('mouseup', unset_holding_lmb)
    scene.bind("mousedown", set_holding_lmb )

    scene.bind("mousemove", drag_container_pickup )

if __name__ == "__main__":
    main()