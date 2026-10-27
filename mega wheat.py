def wheat():
	while True:
		harvest()
		move(North)
clear()
for i in range(max_drones() - 1):
	spawn_drone(wheat)
	move(East)
wheat()