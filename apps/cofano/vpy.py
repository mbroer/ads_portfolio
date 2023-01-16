import gui
import devgui
import camera
import scenario_loader
import grid
import container

from vpython import *

def vector_multiply(vector1, vector2):
    temp = vector1

    temp.x *= vector2.x
    temp.y *= vector2.y
    temp.z *= vector2.z

    return temp

def vector_abs_dist(vec):
    return abs(vec.x) + abs(vec.y) + abs(vec.z)

def process(ev):
    #mousepos = ev.pos
    #get_closest_container(mousepos)
    print(ev.event, ev.which, scene.mouse.pos)

if __name__ == '__main__':
    scene = canvas(title='', width=800, height=450, center=vector(0,0,0), background=color.white)
    #scene.bind('click keydown', process)

    scene.camera.pos = vector(-260.417, 175.102, 322.035)
    scene.camera.axis = vector(260.417, -175.102, -322.035)
    scene.camera.og_pos = scene.camera.pos
    scene.camera.og_axis = scene.camera.axis

    scenario_loader.init(scene)

    grid.grid_ui(scene)
    container.container_ui(scene)

    gui.main(scene)
    devgui.main(scene)
    camera.main(scene)
