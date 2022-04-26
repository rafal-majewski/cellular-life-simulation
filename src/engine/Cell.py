from src.utils.dim2.FloatDim2 import FloatDim2
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.engine.BoundingBox2 import BoundingBox2
from src.utils.color.Color import Color


class Cell:
	def __init__(
		self,
		*,
		position: FloatPoint2,
		velocity: FloatPoint2 = None,
		mass: float,
		radius: float,
		color: Color,

	) -> None:
		self.position: FloatPoint2 = position
		self.velocity: FloatPoint2 = \
			FloatPoint2(0, 0) if velocity is None else velocity
		self.mass: float = mass
		self.radius: float = radius
		self.color: Color = color

	@property
	def position(self) -> FloatPoint2:
		return self._position

	@position.setter
	def position(self, position: FloatPoint2) -> None:
		self._position = position

	@property
	def velocity(self) -> FloatPoint2:
		return self._velocity

	@velocity.setter
	def velocity(self, velocity: FloatPoint2) -> None:
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
			size=FloatDim2(self.radius * 2, self.radius * 2),
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
