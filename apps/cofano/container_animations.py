from vpython import *
from time import sleep

selected_container = None
def container_select_anim(container):
	global selected_container

	if selected_container == container: #deselect
		selected_container = None
		return

	count = 0
	toggle = True
	og_color = container.color
	selected_container = container

	while selected_container == container:

		count += 1

		if count % 60 == 0:
			toggle = not toggle

		calc = vector(0.01,0.01,0.01) if toggle else vector(-0.01,-0.01,-0.01)

		container.set_color( (container.color + calc) )

		sleep(.005)

	container.set_color(og_color)

def container_blocked_anim(selected, container):

	count = 0
	og_color = container.color
	toggle = True

	while selected_container == selected:
		count += 1

		if count % 60 == 0:
			toggle = not toggle

		calc = vector(0.02,0.02,0.02) if toggle else vector(-0.02,-0.02,-0.02)

		container.set_color( (container.color - calc) )

		sleep(.005)


	container.set_color(og_color)