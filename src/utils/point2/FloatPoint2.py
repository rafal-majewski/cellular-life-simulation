from __future__ import annotations
from src.utils.dim2.Dim2 import Dim2
from src.utils.point2.Point2 import Point2
import math


class FloatPoint2(Point2[float]):
	def __str__(self) -> str:
		return f"FloatPoint2({self.x}, {self.y})"

	def __repr__(self) -> str:
		return f"FloatPoint2({self.x}, {self.y})"

	@property
	def magnitude(self) -> float:
		return (self.x ** 2 + self.y ** 2) ** 0.5

	def normalize(self) -> FloatPoint2:
		return FloatPoint2(self.x / self.magnitude, self.y / self.magnitude)

	def __add__(self, other: Point2[float]) -> FloatPoint2:
		return FloatPoint2(self.x + other.x, self.y + other.y)

	def __sub__(self, other: Point2[float]) -> FloatPoint2:
		return FloatPoint2(self.x - other.x, self.y - other.y)

	def __mul__(self, scalar: float) -> FloatPoint2:
		return FloatPoint2(self.x * scalar, self.y * scalar)

	def __rmul__(self, scalar: float) -> FloatPoint2:
		return FloatPoint2(self.x * scalar, self.y * scalar)

	def __truediv__(self, scalar: float) -> FloatPoint2:
		return FloatPoint2(self.x / scalar, self.y / scalar)

	def __rtruediv__(self, scalar: float) -> FloatPoint2:
		return FloatPoint2(self.x / scalar, self.y / scalar)

	def multiplyComponents(self, other: Point2[float]) -> FloatPoint2:
		return FloatPoint2(self.x * other.x, self.y * other.y)

	def divideComponents(self, other: Point2[float]) -> FloatPoint2:
		return FloatPoint2(self.x / other.x, self.y / other.y)

	@staticmethod
	def fromDim2(dim: Dim2[float]) -> FloatPoint2:
		return FloatPoint2(float(dim.width), float(dim.height))

	def dotProduct(self, other: Point2[float]) -> float:
		return self.x * other.x + self.y * other.y

	def round(self) -> FloatPoint2:
		return FloatPoint2(round(self.x), round(self.y))

	def floor(self) -> FloatPoint2:
		return FloatPoint2(math.floor(self.x), math.floor(self.y))

	def ceil(self) -> FloatPoint2:
		return FloatPoint2(math.ceil(self.x), math.ceil(self.y))

	@staticmethod
	def fromPoint2(point: Point2) -> FloatPoint2:
		return FloatPoint2(float(point.x), float(point.y))
