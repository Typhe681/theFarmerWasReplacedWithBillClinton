import movement
def start(size, oX, oY):
	X = []
	Y = []
	movement.goto(oX, oY)
	for x in range(size):
		movement.goto(x + oX, get_pos_y())
		north = (x % 2 == 0)
		for y in range(size):
			if can_harvest() or get_entity_type() != Entities.Pumpkin:
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			X.append(get_pos_x())
			Y.append(get_pos_y())
			if y != size - 1:
				if north:
					move(North)
				else:
					move(South)
	while X:
		i = 0
		while i < len(X):
			movement.goto(X[i], Y[i])
			if can_harvest():
				X.pop(i)
				Y.pop(i)
			else:
				i += 1
				plant(Entities.Pumpkin)
	harvest()