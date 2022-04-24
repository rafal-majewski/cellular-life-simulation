import pygame
from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer
from src.engine.Cell import Cell
from src.utils.Point2 import Point2
from src.engine.Joint import Joint
from src.engine.physics.CollisionResolver import CollisionResolver
from src.engine.physics.JointResolver import JointResolver
from src.engine.physics.MovementResolver import MovementResolver
import random
import math


if __name__ == "__main__":
	pygame.init()
	surface: pygame.surface.Surface = pygame.display.set_mode((800, 600))
	drawer: Drawer = Drawer(surface)
	world: World = World(
		collisionResolver=CollisionResolver(),
		jointResolver=JointResolver(),
		movementResolver=MovementResolver(),
	)
	camera: AbstractCamera = Camera(drawer=drawer, position=Point2(0, 0))
	game: Game = Game(world=world, camera=camera)
	game.start()
