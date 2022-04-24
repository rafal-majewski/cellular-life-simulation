from src.utils.Point2 import Point2
from src.utils.Dim2 import Dim2
from src.engine.BoundingBox2 import BoundingBox2


class Cell:
	def __init__(
		self,
		*,
		position: Point2,
		velocity: Point2 = None,
		mass: float,
		radius: float,
	) -> None:
		self.position: Point2 = position
		self.velocity: Point2 = Point2(0, 0) if velocity is None else velocity
		self.mass: float = mass
		self.radius: float = radius

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

	@property
	def boundingBox(self) -> BoundingBox2:
		return BoundingBox2(
			center=self.position,
			size=Dim2(self.radius * 2, self.radius * 2),
		)

	def __str__(self) -> str:
		return (
			f"Cell("
			f"position={self.position}, "
			f"velocity={self.velocity}, "
			f"mass={self.mass}, "
			f"radius={self.radius}"
			f")"
		)
