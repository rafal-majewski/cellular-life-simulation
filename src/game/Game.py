import random
from typing import Optional
from src.camera.Camera import Camera
from src.engine.World import World
from src.engine.atoms.air.Air import Air
import time
from src.config.gameconfig.GameConfig import GameConfig
from src.config.gameconfig.worldconfig.atomsconfig.airconfig.AirConfig import AirConfig
from src.utils.point2.FloatPoint2 import FloatPoint2


class Game:
	def __init__(
		self,
		*,
		world: World,
		camera: Camera,
		config: GameConfig,
	) -> None:
		self.world: World = world
		self.camera: Camera = camera
		self._lastTickTimestamp: Optional[float] = None
		self._config: GameConfig = config
		self._frameTime: float = 1 / self._config.fps

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
		return FloatPoint2.fromDim2(self._config.world.size / 2) \
			.multiplyComponents(
				FloatPoint2(random.uniform(-1, 1), random.uniform(-1, 1))
		)

	def createAir(self) -> Air:
		airConfig: AirConfig = self._config.world.atoms.air
		air: Air = Air(
			position=self.generateRandomPosition(),
			velocity=FloatPoint2(random.uniform(-50, 50), random.uniform(-50, 50)),
			radius=airConfig.radius,
			mass=airConfig.mass,
			color=airConfig.color,
		)
		return air

	def spawnAir(self) -> None:
		air: Air = self.createAir()
		self.world.addAtom(air)

	def start(self) -> None:
		for i in range(280):
			self.spawnAir()
		self.display()
		while True:
			self.tick()
