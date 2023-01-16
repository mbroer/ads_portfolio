boats = dict()
boat_ids = 0
class Boat:
	def __init__(self, color, num_containers=None, id=None):
		global boat_ids
		self.color = color
		self.num_containers = num_containers
		boat_ids += 1
		self.id = boat_ids if id is None else id

		boats[self.id] = self

	def remove(self):
		del boats[self.id]

def get_by_id(id):
	return boats[id]