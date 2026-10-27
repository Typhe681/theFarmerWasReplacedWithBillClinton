#size should be at least 7 (9 with power)
#otherwise some trees dont grow fast enough
import movement
def start(size, oX, oY):
	movement.goto(oX, oY)
	for x in range(size):
		movement.goto(x + oX, get_pos_y())
		north = (x % 2 == 0)
		for y in range(size):
			if can_harvest():
				harvest()
			elif get_entity_type() != Entities.Tree:
				if get_entity_type() != Entities.Bush:
					harvest()
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			if y != size - 1:
				if north:
					move(North)
				else:
					move(South)