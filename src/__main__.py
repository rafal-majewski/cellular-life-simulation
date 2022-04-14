from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.engine.World import World
from pygame import Surface
from src.pygameimp.Drawer import Drawer


if __name__ == "__main__":
	drawer = Drawer(Surface((100, 100)))
	world = World()
	camera = Camera(drawer)
	game = Game(world=world, camera=camera)
