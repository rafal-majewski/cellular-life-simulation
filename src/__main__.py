import pygame
from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer
from src.engine.Cell import Cell
from src.utils.Point2 import Point2
from src.engine.Joint import Joint
import random
import math


if __name__ == "__main__":
	pygame.init()
	surface: pygame.surface.Surface = pygame.display.set_mode((800, 600))
	drawer: Drawer = Drawer(surface)
	world: World = World()

	# for i in range(30):
	# 	radius = 14
	# 	wall = Cell(
	# 		position=Point2(
	# 			x=-200,
	# 			y=-300 + i * radius * 2
	# 		),
	# 		velocity=Point2(
	# 			x=0,
	# 			y=0
	# 		),
	# 		radius=radius,
	# 		mass=300000
	# 	)
	# 	world.addCell(wall)

	for i in range(30):
		headRadius = random.random() * 14 + 8
		head = Cell(
			position=Point2(
				random.random() * 800 - 400,
				random.random() * 600 - 300
			),
			velocity=Point2(
				random.random() * 11 - 5,
				random.random() * 11 - 5
			),
			mass=headRadius ** 2 * math.pi,
			radius=headRadius
		)
		world.addCell(head)
		cellBefore = head
		for j in range(random.randint(1, 1)):
			# print(j)
			angle = 0
			# random.random() * math.pi * 2
			radius = random.random() * 14 + 8
			cell: Cell = Cell(
				position=Point2(
					cellBefore.position.x + math.cos(angle) * (cellBefore.radius + radius),
					cellBefore.position.y + math.sin(angle) * (cellBefore.radius + radius)
				),
				velocity=Point2(
				random.random() * 11 - 5,
				random.random() * 11 - 5
				),
				mass=radius**2 * math.pi,
				radius=radius
			)
			world.addCell(cell)
			joint: Joint = Joint(
				cell1=cellBefore,
				cell2=cell,
				stiffness=random.random() * 0.1 + 0.1
			)
			world.addJoint(joint)
			cellBefore = cell
	
	# for i in range(0, 80):
	# 	radius = int((random.random()) ** 0.2 * (random.random()) * 40)
	# 	mass = radius ** 2 * math.pi
	# 	world.addCell(
	# 		Cell(
	# 			position=Point2(
	# 				random.random() * 800 - 400,
	# 				random.random() * 600 - 300
	# 			),
	# 			velocity=Point2(
	# 				random.random() * 40 - 20,
	# 				random.random() * 40 - 20
	# 			),
	# 			mass=mass,
	# 			radius=radius
	# 		)
	# 	)
	camera: AbstractCamera = Camera(drawer=drawer, position=Point2(0, 0))
	game: Game = Game(world=world, camera=camera)
	game.start()
