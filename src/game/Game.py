from typing import Optional
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
import time


class Game:
	def __init__(
		self,
		*,
		world: World,
		camera: AbstractCamera,
	) -> None:
		self.world: World = world
		self.camera: AbstractCamera = camera
		self.lastDisplayTimestamp: Optional[float] = None

	def display(self) -> None:
		self.lastDisplayTimestamp = time.time()
		self.camera.display(self.world)

	def start(self) -> None:
		self.display()
		while True:
			currentTimestamp: float = time.time()
			deltaTime: float = currentTimestamp - (self.lastDisplayTimestamp or time.time())
			self.world.tick(deltaTime)
			self.display()
