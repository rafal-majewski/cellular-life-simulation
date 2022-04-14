import pygame
from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer
from src.engine.Cell import Cell
from src.utils.Point2 import Point2
import random


if __name__ == "__main__":
	pygame.init()
	surface: pygame.surface.Surface = pygame.display.set_mode((800, 600))
	drawer: Drawer = Drawer(surface)
	world: World = World()
	for i in range(0, 1000):
		world.addCell(
			Cell(
				position=Point2(
					random.random() * 800 - 400,
					random.random() * 600 - 300
				),
				mass=1,
				radius=(random.random()) ** 0.2 * (random.random()) * 20
			)
		)
	camera: AbstractCamera = Camera(drawer=drawer, position=Point2(0, 0))
	game: Game = Game(world=world, camera=camera)
	game.start()
