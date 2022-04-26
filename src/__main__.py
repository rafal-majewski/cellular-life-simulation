import pygame
from src.game.Game import Game
from src.pygameimp.Camera import PygameCamera
from src.camera.Camera import Camera
from src.engine.world.World import World
from src.pygameimp.Drawer import Drawer
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.utils.dim2.IntDim2 import IntDim2
from src.engine.physics.collisionresolver.CollisionResolver import CollisionResolver
from src.engine.physics.jointresolver.JointResolver import JointResolver
from src.engine.physics.movementresolver.MovementResolver import MovementResolver
import json
from src.config.Config import Config


def main(config: Config):
	pygame.init()
	surface: pygame.surface.Surface = pygame.display.set_mode(config.window.size.toTuple())
	drawer: Drawer = Drawer(surface)
	world: World = World(
		collisionResolver=CollisionResolver(),
		jointResolver=JointResolver(),
		movementResolver=MovementResolver(),
		config=config.world,
	)
	camera: Camera = PygameCamera(drawer=drawer, position=FloatPoint2(0, 0))
	game: Game = Game(
		world=world,
		camera=camera,
		config=config.game,
	)
	game.start()

if __name__ == "__main__":
	with open("config.json", "r") as configFile:
		config: Config = Config.fromJson(json.load(configFile))
		main(config)
