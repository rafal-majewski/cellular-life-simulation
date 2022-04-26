import random
from typing import Optional
from src.camera.Camera import Camera
from src.world.World import World
from src.world.atoms.air.Air import Air
import time
from src.config.game.GameConfig import GameConfig
from src.config.world.atoms.air.AirConfig import AirConfig
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.creature.Creature import Creature
from src.creature.builder.CreatureBuilder import CreatureBuilder
from src.creature.genesmanager.GenesManager import GenesManager


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
		return FloatPoint2.fromDim2(self.world.size / 2) \
			.multiplyComponents(
				FloatPoint2(random.uniform(-1, 1), random.uniform(-1, 1))
		)

	def createAir(self) -> Air:
		airConfig: AirConfig = self.world.config.atoms.air
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

	def spawnCreature(self, creature: Creature) -> None:
		# print(creature)
		for cell in creature.cells:
			print(cell)
			self.world.addAtom(cell)
		for joint in creature.joints:
			self.world.addJoint(joint)


	def start(self) -> None:
		# for _ in range(180):
		# 	self.spawnAir()
		for _ in range(10):
			self.spawnCreature(
				CreatureBuilder.build(
					genesManager=GenesManager.generateRandom()
				)
			)
		self.display()
		while True:
			self.tick()
