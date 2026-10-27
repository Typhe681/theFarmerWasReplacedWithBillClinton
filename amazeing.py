clear()
import movement
dirs = [North, East, South, West]
dir = 0

def thingy():
	place = random()*get_world_size()//1
	movement.wrapto(place, place)
	dir = 0
	while True:
		while get_entity_type() != Entities.Treasure:
			for turn in [1, 0, -1, 2]:
				new_dir = (dir + turn) % 4
				if can_move(dirs[new_dir]):
					dir = new_dir
					move(dirs[dir])
					break
		harvest()

spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
spawn_drone(thingy)
do_a_flip()

while True:
	while get_entity_type() != Entities.Treasure:
		if get_entity_type() != Entities.Hedge:
			plant(Entities.Bush)
			use_item(Items.Weird_Substance, get_world_size() * 32)
		for turn in [1, 0, -1, 2]:
			new_dir = (dir + turn) % 4
			if can_move(dirs[new_dir]):
				dir = new_dir
				move(dirs[dir])
				break
	harvest()