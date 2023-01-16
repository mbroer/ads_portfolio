from vpython import button
import datetime

import json
import container as c
import grid as g
import boat as b


def init(_scene):
	button( bind=save_scenario, text='Save scenario', pos=_scene.title_anchor )

def save_scenario():
	grid = g.get_grid()
	containers = c.containers
	boats = b.boats.values()

	string = f'{{"grid": {{"rows": {grid.rows}, "columns": {grid.columns}, "stacks": {grid.stacks} }},'

	string += f'"ships": ['

	for boat in boats:
		col = boat.color
		string += f'{{"id": {boat.id}, "color": [{col.x},{col.y},{col.z}]}},'

	string = string[:-1]

	string += f'],'

	string += f'"containers": ['

	for container in containers:
		string += f'{{"id": {container.id}, "shipid": {container.boatid}, "placement": [{container.row},{container.column},{container.stack}] }},'

	string = string[:-1]

	string += f'],'

	string += f'"moves": {{}}'

	string += '}'

	print(string)

	now = datetime.datetime.now()

	timestamp = now.strftime("%Y-%m-%d %H %M %S")

	with open(f"scenarios/{timestamp}.json", "w") as file:
		json.dump(json.loads(string), file, indent=4)
