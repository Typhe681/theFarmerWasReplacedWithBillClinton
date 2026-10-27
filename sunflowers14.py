import movement
def start(oX, oY):
	def thingmajig(x, oY):
		while True:
			movement.goto(x, oY)
			for y in range(14):
				if can_harvest() or get_entity_type() != Entities.Sunflower:
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
				if y != 13:
					move(North)
			move(East)
			for y in range(14):
				if can_harvest() or get_entity_type() != Entities.Sunflower:
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Sunflower)
				if y != 13:
					move(South)
	movement.goto(oX, oY)
	drones = []
	for x in range(6):
		drones.append(spawn_drone(thingmajig, oX + x*2 + 2, oY))
	thingmajig(oX, oY)