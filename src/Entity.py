from abc import ABC
from src.Point2 import Point2


class Entity(ABC):
	def __init__(self, *, position: Point2, velocity: Point2) -> None:
		self._position = position
		self._velocity = velocity

	@property
	def position(self) -> Point2:
		return self._position

	@position.setter
	def position(self, position: Point2) -> None:
		self._position = position

	@property
	def velocity(self) -> Point2:
		return self._velocity

	@velocity.setter
	def velocity(self, velocity: Point2) -> None:
		self._velocity = velocity
