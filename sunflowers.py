#ONLY HAVE ONE DRONE DOING SUNFLOWERS OR IT WONT GIVE MAX AMOUNT
import movement
def start(size, oX, oY):
	X = []
	Y = []
	P1 = []
	P2 = []
	def max(numbers):
		highest = numbers[0]
		indices = [0]
		for i in range(1, len(numbers)):
			if numbers[i] > highest:
				highest = numbers[i]
				indices = [i]
			elif numbers[i] == highest:
				indices.append(i)
		return indices

	movement.goto(oX, oY)
	for x in range(size):
		movement.goto(x + oX, get_pos_y())
		north = (x % 2 == 0)
		for y in range(size):
			if can_harvest() or get_entity_type() != Entities.Sunflower:
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
			P1.append(measure())
			X.append(get_pos_x())
			Y.append(get_pos_y())
			if y != size - 1:
				if north:
					move(North)
				else:
					move(South)
	while X:
		P2 = max(P1)
		for i in range(len(P2) - 1, -1, -1):
			iMax = P2[i]
			movement.goto(X[iMax], Y[iMax])
			while not can_harvest():
				pass
			X.pop(iMax)
			Y.pop(iMax)
			P1.pop(iMax)
			harvest()