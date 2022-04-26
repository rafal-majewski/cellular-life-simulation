from src.utils.movable.Movable import Movable
from src.world.utils.boundingbox2.BoundingBox2 import BoundingBox2
from abc import abstractmethod


class Entity(Movable):
	@property
	@abstractmethod
	def boundingBox(self) -> BoundingBox2:
		pass
