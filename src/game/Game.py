import random
from typing import Optional
from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
from src.engine.Air import Air
import time

from src.utils.point2.FloatPoint2 import FloatPoint2


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

	def generateRandomPosition(self) -> FloatPoint2:
		return FloatPoint2.fromDim2(self.world.size / 2) \
			.multiplyComponents(
				FloatPoint2(random.uniform(-1, 1), random.uniform(-1, 1))
		)

	def createAir(self) -> Air:
		air: Air = Air(
			position=self.generateRandomPosition(),
			velocity=FloatPoint2(random.uniform(-10, 10), random.uniform(-10, 10)),
		)
		return air

	def spawnAir(self) -> None:
		air: Air = self.createAir()
		self.world.addCell(air)

	def start(self) -> None:
		for i in range(280):
			self.spawnAir()
		self.display()
		while True:
			self.tick()
