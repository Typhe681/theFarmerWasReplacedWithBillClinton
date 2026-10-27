import movement
import wheat
import wood
import carrots
import pumpkins
import sunflowers14
import cacti
import maze

def wheatloop(size, oX, oY):
	while True:
		wheat.start(size, oX, oY)
		
def woodloop(size, oX, oY):
	while True:
		wood.start(size, oX, oY)
		
def carrotloop(size, oX, oY):
	while True:
		carrots.start(size, oX, oY)

def pumpkinloop(size, oX, oY):
	while True:
		pumpkins.start(size, oX, oY)

def sunflowerloop(size, oX, oY):
	while True:
		sunflowers14.start(oX, oY)

def cactiloop(size, oX, oY):
	while True:
		cacti.start(size, oX, oY)

def mazeloop(size, oX, oY):
	while True:
		maze.start(size, oX, oY, True)

clear()
while True:
	spawn_drone(cactiloop,     10, 7, 7)
	spawn_drone(mazeloop,      10, 12, 22)
	spawn_drone(mazeloop,      10, 22, 12)
	spawn_drone(sunflowerloop, 14, 17, 17)
	spawn_drone(pumpkinloop,   6, 1, 1)
	spawn_drone(carrotloop,    6, 1, 7)
	spawn_drone(carrotloop,    6, 7, 1)
	spawn_drone(pumpkinloop,   6, 1, 13)
	spawn_drone(pumpkinloop,   6, 13, 1)
	spawn_drone(carrotloop,    6, 1, 19)
	spawn_drone(carrotloop,    6, 19, 1)
	spawn_drone(woodloop,      6, 1, 25)
	spawn_drone(woodloop,      6, 25, 1)
	spawn_drone(wheatloop,     32, 0, 0)
	do_a_flip()
	wheatloop(32, 0, 0)