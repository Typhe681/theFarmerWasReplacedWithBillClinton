def goto(x, y):
	while get_pos_x() < x:
		move(East)
	while get_pos_x() > x:
		move(West)
	while get_pos_y() < y:
		move(North)
	while get_pos_y() > y:
		move(South)

def wrapto(x, y):
	size = get_world_size()
	dx = (x - get_pos_x()) % size
	dy = (y - get_pos_y()) % size
	
	if dx <= size // 2:
		xDir = East
		xSteps = dx
	else:
		xDir = West
		xSteps = size - dx
	
	if dy <= size // 2:
		yDir = North
		ySteps = dy
	else:
		yDir = South
		ySteps = size - dy
	
	for i in range(xSteps):
		move(xDir)
	for i in range(ySteps):
		move(yDir)