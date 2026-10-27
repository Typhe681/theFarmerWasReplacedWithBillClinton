def aaa():
	while True:
		use_item(Items.Fertilizer)
		harvest()
clear()
for i in range(max_drones() - 1):
	spawn_drone(aaa)
	move(East)
aaa()