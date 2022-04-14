import pygame
from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
import pygame
from src.pygameimp.Drawer import Drawer


if __name__ == "__main__":
	pygame.init()
	surface: pygame.surface.Surface = pygame.display.set_mode((800, 600))
	drawer: Drawer = Drawer(pygame.display.set_mode((800, 600)))
	world: World = World()
	camera: AbstractCamera = Camera(drawer)
	game: Game = Game(world=world, camera=camera)
	game.start()