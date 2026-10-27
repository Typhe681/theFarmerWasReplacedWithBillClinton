#size should be at least 6 (9 with power)
#otherwise some carrots dont grow fast enough
import movement
def start(size, oX, oY):
	movement.goto(oX, oY)
	for x in range(size):
		movement.goto(x + oX, get_pos_y())
		north = (x % 2 == 0)
		for y in range(size):
			if can_harvest() or get_entity_type() != Entities.Carrot:
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Carrot)
			if y != size - 1:
				if north:
					move(North)
				else:
					move(South)