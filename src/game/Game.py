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
		fps: float = 60,
	) -> None:
		self.world: World = world
		self.camera: AbstractCamera = camera
		self._lastTickTimestamp: Optional[float] = None
		self.fps: float = fps

	@property
	def fps(self) -> float:
		return self._fps

	@fps.setter
	def fps(self, fps: float) -> None:
		self._fps = fps
		self._frameTime = 1 / fps

	def display(self) -> None:
		self.camera.display(self.world)

	def tick(self) -> None:
		currentTickTimestamp: float = time.time()
		deltaTime: float = \
			currentTickTimestamp \
			- (self._lastTickTimestamp or time.time())
		self._lastTickTimestamp = time.time()
		self.world.tick(deltaTime)
		self.display()
		time.sleep(max(0, self._frameTime - (time.time() - self._lastTickTimestamp)))

	def start(self) -> None:
		self.display()
		while True:
			self.tick()
