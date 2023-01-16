import json
import container as cont
import boat
import grid
from vpython import vector, menu, button, checkbox
import glob, os
from time import sleep
import scenario_saver as ss

loaded_scenario = None
scenario_menu = None

def init(_scene):
	global scenario_menu

	_scene.append_to_title('<h4>Scenario settings</h4>')

	checkbox(bind=set_low_detail, pos=_scene.title_anchor, text='Low detail', checked=cont.low_detail)
	_scene.append_to_title('\n')

	scenario_menu = menu( bind=load_scenario, choices=[], pos=_scene.title_anchor)
	button(bind=refresh_scenario, text='↺', pos=_scene.title_anchor )

	_scene.append_to_title('\t')
	button( bind=unload_scenario, text='Unload scenario', pos=_scene.title_anchor )
	button( bind=reload_scenario, text='Reload scenario', pos=_scene.title_anchor )

	ss.init(_scene)

	_scene.append_to_title('\n<hr>')

	refresh_scenario()

def set_low_detail(evt):
	cont.low_detail = evt.checked

def refresh_scenario():
	global scenario_menu
	scenario_menu.choices = ['Select scenario'] + [os.path.basename(x) for x in os.listdir('./scenarios')]


done_loading = True
def load_scenario(e):
	global loaded_scenario
	global done_loading

	while not done_loading:
		sleep(.1)

	done_loading = False

	scenario = e.selected

	if e.index == loaded_scenario:
		return

	if loaded_scenario is not None:
		unload_scenario(False)

	loaded_scenario = e.index

	if e.index == 0:
		loaded_scenario = None
		return

	print(f"Loading {scenario}")

	with open(f'scenarios/{scenario}', 'r') as f:
		data = json.load(f)
	
	for ship in data['ships']:
		boat.Boat(id=ship['id'], color=vector(ship['color'][0],ship['color'][1],ship['color'][2]))

	grid.Grid(boat.boats, data['grid']['rows'], data['grid']['columns'], data['grid']['stacks'])

	for container in data['containers']:
		cont.Container( boat=boat.get_by_id(container['shipid']), position=vector(container['placement'][0], container['placement'][1], container['placement'][2]), id=container['id'] )

	cont.post_init()

	print(f"Loaded {scenario}")
	done_loading = True


def reload_scenario():
	global scenario_menu
	temp = scenario_menu.selected
	scenario_menu.selected = 0

	unload_scenario()
	scenario_menu.selected = temp
	load_scenario(scenario_menu)


def unload_scenario(reset_menu_choice=True):
	global loaded_scenario
	global scenario_menu

	if reset_menu_choice:
		scenario_menu.index = 0

	print("Unloading scenario")

	loaded_scenario = None

	boat.boats = dict()
	boat.boat_ids = 0

	for c in cont.containers.copy():
		c.remove()

	grid.grid.remove()

	cont.containers = list()

	cont.containers_stack = list()

	cont.containers = list()
	cont.containers_stack = dict()

