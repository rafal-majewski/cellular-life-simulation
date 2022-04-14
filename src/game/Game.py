from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World


class Game:
	def __init__(
		self,
		*,
		world: World,
		camera: AbstractCamera,
	) -> None:
		self.world = world
		self.camera = camera

	def start(self) -> None:
		while True:
			self.camera.display(self.world)
