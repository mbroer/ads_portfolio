from vpython import *
import container as cont


scene = None
selected_container = None

def inputbox(s):
    print(s.text, s.number)
    #text = s.text.split(',')
    #for container in cont.containers:
    #     container.textobj2.axis = vector(float(text[0]), float(text[1]), float(text[2]))


def B(b):
    cont.containers[1].move_to(2,2)
    print(scene.camera.pos)
    print(scene.camera.axis)



def xy_parse(s):
    global selected_container

    splits = s.text.split(',')
    x = int(splits[0])
    y = int(splits[1])

    if selected_container is None:
        selected_container = cont.containers[0]

    selected_container.move_to(x,y,None, True)

def main(_scene=None):
    global scene
    scene = _scene
    winput( bind=inputbox )
    button( bind=B, text='dev' )
    
    winput( bind=xy_parse, type="string" )

if __name__ == "__main__":
    main()