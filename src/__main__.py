import pygame
from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer
from src.engine.Cell import Cell
from src.engine.Point2 import Point2


if __name__ == "__main__":
	pygame.init()
	surface: pygame.surface.Surface = pygame.display.set_mode((800, 600))
	drawer: Drawer = Drawer(surface)
	world: World = World()
	world.addCell(Cell(position=Point2(0, 0), mass=1, radius=10))
	camera: AbstractCamera = Camera(drawer)
	game: Game = Game(world=world, camera=camera)
	game.start()
