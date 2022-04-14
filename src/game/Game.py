from src.abstractcamera import AbstractCamera
from src.engine import World


class Game:
	def __init__(
		self,
		*
		world: World,
		camera: AbstractCamera,
	) -> None:
		self.world = world
		self.camera = camera

	def start(self) -> None:
		pass
		# self.camera.display(self.world)
