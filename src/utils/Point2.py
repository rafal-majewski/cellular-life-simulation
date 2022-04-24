from __future__ import annotations
from typing import Any
from src.utils.Dim2 import Dim2


class Point2:
	def __init__(self, x: float, y: float) -> None:
		self._x = x
		self._y = y

	@property
	def x(self) -> float:
		return self._x

	@property
	def y(self) -> float:
		return self._y

	@staticmethod
	def fromDim2(dim: Dim2) -> Point2:
		return Point2(dim.width, dim.height)

	def __str__(self) -> str:
		return f"Point2({self.x}, {self.y})"

	def __repr__(self) -> str:
		return f"Point2({self.x}, {self.y})"

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Point2):
			return False
		return self.x == other.x and self.y == other.y

	def __add__(self, other: Point2) -> Point2:
		return Point2(self.x + other.x, self.y + other.y)

	def __sub__(self, other: Point2) -> Point2:
		return Point2(self.x - other.x, self.y - other.y)

	def __mul__(self, scalar: float) -> Point2:
		return Point2(self.x * scalar, self.y * scalar)

	def __rmul__(self, scalar: float) -> Point2:
		return Point2(self.x * scalar, self.y * scalar)

	def __truediv__(self, scalar: float) -> Point2:
		return Point2(self.x / scalar, self.y / scalar)

	def __rtruediv__(self, scalar: float) -> Point2:
		return Point2(self.x / scalar, self.y / scalar)

	def multiplyComponents(self, other: Point2) -> Point2:
		return Point2(self.x * other.x, self.y * other.y)

	@property
	def magnitude(self) -> float:
		return (self.x ** 2 + self.y ** 2) ** 0.5

	def dotProduct(self, other: Point2) -> float:
		return self.x * other.x + self.y * other.y

	def normalize(self) -> Point2:
		return self / self.magnitude
