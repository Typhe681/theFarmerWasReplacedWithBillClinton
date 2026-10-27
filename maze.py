#spawns the maze centered on the drone, so gotta offset more
import movement
def start(size, oX, oY, twin):
	dirs = [North, East, South, West]
	movement.goto(oX, oY)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, size * 32)
	def twinjamin():
		dir = 0
		while get_entity_type() == Entities.Hedge or get_entity_type() == Entities.Treasure:
			if get_entity_type() == Entities.Treasure:
				harvest()
			else:
				for turn in [-1, 0, 1, 2]:
					new_dir = (dir + turn) % 4
					if can_move(dirs[new_dir]):
						dir = new_dir
						move(dirs[dir])
						break
	if twin == True:
		spawn_drone(twinjamin)
	dir = 0
	while get_entity_type() == Entities.Hedge or get_entity_type() == Entities.Treasure:
		if get_entity_type() == Entities.Treasure:
			harvest()
		else:
			for turn in [1, 0, -1, 2]:
				new_dir = (dir + turn) % 4
				if can_move(dirs[new_dir]):
					dir = new_dir
					move(dirs[dir])
					break