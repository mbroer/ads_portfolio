from vpython import *
import container as cont
import grid
import scenario_loader

scene

def camera_reset():
    scene.camera.axis = scene.camera.og_axis
    scene.camera.pos = scene.camera.og_pos

    print(scene.camera.axis)

def main(_scene=None):
    global scene
    scene = _scene

    _scene.append_to_caption('<h4>Extra</h4>')

    button( bind=camera_reset, text='Reset camera' )

    _scene.append_to_caption('<hr>')

    print("gui loaded")

if __name__ == "__main__":
    main()