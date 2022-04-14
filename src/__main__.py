from src.game.Game import Game
from src.pygameimp.Camera import Camera
from src.engine.World import World


if __name__ == "__main__":
	world = World()
	camera = Camera()
	game = Game(world=world, camera=camera)
