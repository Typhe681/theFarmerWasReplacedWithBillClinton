import movement
def sort_column(size, oX, oY):
	x = get_pos_x()
	for y in range(size):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		if y != size - 1:
			move(North)
	movement.goto(x, oY)
	swapped = True
	going_north = True
	low = oY
	high = oY + size - 1
	while swapped:
		if going_north:
			swapped = False
			if low > oY:
				move(North)
			else:
				movement.goto(x, low)
			for i in range(high - low):
				if measure() > measure(North):
					swap(North)
					swapped = True
				move(North)
			high -= 1
		else:
			move(South)
			for i in range(high - low):
				if measure() < measure(South):
					swap(South)
					swapped = True
				move(South)
			low += 1
		going_north = not going_north

def sort_row(size, oX, oY):
	y = get_pos_y()
	swapped = True
	going_east = True
	low = oX
	high = oX + size - 1
	while swapped:
		if going_east:
			swapped = False
			if low > oX:
				move(East)
			else:
				movement.goto(low, y)
			for i in range(high - low):
				if measure() > measure(East):
					swap(East)
					swapped = True
				move(East)
			high -= 1
		else:
			move(West)
			for i in range(high - low):
				if measure() < measure(West):
					swap(West)
					swapped = True
				move(West)
			low += 1
		going_east = not going_east

def start(size, oX, oY):
	drones = []
	movement.goto(oX, oY)
	for i in range(size - 1):
		drones.append(spawn_drone(sort_column, size, oX, oY))
		if i != size - 1:
			move(East)
	sort_column(size, oX, oY)
	for drone in drones:
		wait_for(drone)
	movement.goto(oX, oY)
	for i in range(size - 1):
		drones.append(spawn_drone(sort_row, size, oX, oY))
		if i != size - 1:
			move(North)
	sort_row(size, oX, oY)
	for drone in drones:
		wait_for(drone)
	movement.goto(oX, oY)
	harvest()