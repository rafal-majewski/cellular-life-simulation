from __future__ import annotations
from src.utils.point2.Point2 import Point2
from src.utils.dim2.Dim2 import Dim2


class IntPoint2(Point2[int]):
	def __init__(self, x: int, y: int) -> None:
		super().__init__(x, y)

	def __str__(self) -> str:
		return f"IntPoint2({self.x}, {self.y})"

	def __repr__(self) -> str:
		return f"IntPoint2({self.x}, {self.y})"

	def __add__(self, other: Point2[int]) -> IntPoint2:
		return IntPoint2(self.x + other.x, self.y + other.y)

	def __sub__(self, other: Point2[int]) -> IntPoint2:
		return IntPoint2(self.x - other.x, self.y - other.y)

	def __mul__(self, scalar: int) -> IntPoint2:
		return IntPoint2(self.x * scalar, self.y * scalar)

	def __rmul__(self, scalar: int) -> IntPoint2:
		return IntPoint2(self.x * scalar, self.y * scalar)

	def __truediv__(self, scalar: float) -> IntPoint2:
		return IntPoint2(int(self.x / scalar), int(self.y / scalar))

	def __rtruediv__(self, scalar: float) -> IntPoint2:
		return IntPoint2(int(self.x / scalar), int(self.y / scalar))

	def multiplyComponents(self, other: Point2[int]) -> IntPoint2:
		return IntPoint2(self.x * other.x, self.y * other.y)

	def divideComponents(self, other: Point2) -> Point2:
		return IntPoint2(self.x / other.x, self.y / other.y)

	@staticmethod
	def fromDim2(dim: Dim2[int]) -> IntPoint2:
		return IntPoint2(dim.width, dim.height)

	def dotProduct(self, other: Point2[int]) -> int:
		return self.x * other.x + self.y * other.y

	@staticmethod
	def fromPoint2(point: Point2) -> IntPoint2:
		return IntPoint2(int(point.x), int(point.y))
