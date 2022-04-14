from src.engine.Entity import Entity
from src.engine.Point2 import Point2


class Cell(Entity):
	def __init__(
		self,
		*,
		position: Point2,
		velocity: Point2,
		mass: float,
		radius: float,
	) -> None:
		super().__init__(position=position, velocity=velocity)
		self.mass = mass
		self.radius = radius

	@property
	def mass(self) -> float:
		return self._mass

	@mass.setter
	def mass(self, mass: float) -> None:
		self._mass = mass

	@property
	def radius(self) -> float:
		return self._radius

	@radius.setter
	def radius(self, radius: float) -> None:
		self._radius = radius
