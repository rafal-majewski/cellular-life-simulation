from typing import Optional
from src.utils.dim2.FloatDim2 import FloatDim2
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.world.utils.boundingbox2.BoundingBox2 import BoundingBox2
from src.utils.color.Color import Color
from src.world.utils.entity.Entity import Entity

class Atom(Entity):
	def __init__(
		self,
		*,
		position: FloatPoint2,
		velocity: Optional[FloatPoint2] = None,
		mass: float,
		radius: float,
		color: Color,
	) -> None:
		super().__init__(
			position=position,
			velocity=velocity,
		)
		self.mass: float = mass
		self.radius: float = radius
		self.color: Color = color

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
			f"Atom("
			f"position={self.position}, "
			f"velocity={self.velocity}, "
			f"mass={self.mass}, "
			f"radius={self.radius}"
			f")"
		)
