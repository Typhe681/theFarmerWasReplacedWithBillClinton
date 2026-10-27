#size MUST be at least 2 (3 with power)
#grass needs time to grow
import movement
def start(size, oX, oY):
	def line(dir, size, i):
		if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
		harvest()
		if get_ground_type() != Grounds.Grassland:
			till()
		if i != size - 1:
			move(dir)
	movement.goto(oX, oY)
	for i in range(size):
		line (North, size, i)
	for i in range(size):
		line (East, size, i)
	for i in range(size):
		line (South, size, i)
	for i in range(size):
		line (West, size, i)