from __future__ import annotations
from typing import Any


class Dim2:
	def __init__(self, width: float, height: float) -> None:
		self._width: float = width
		self._height: float = height

	@property
	def width(self) -> float:
		return self._width

	@property
	def height(self) -> float:
		return self._height

	def __repr__(self) -> str:
		return f"Dim2({self.width}, {self.height})"

	def __str__(self) -> str:
		return f"Dim2({self.width}, {self.height})"

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Dim2):
			return False
		return self.width == other.width and self.height == other.height

	def __add__(self, other: Dim2) -> Dim2:
		return Dim2(self.width + other.width, self.height + other.height)

	def __sub__(self, other: Dim2) -> Dim2:
		return Dim2(self.width - other.width, self.height - other.height)

	def __mul__(self, scalar: float) -> Dim2:
		return Dim2(self.width * scalar, self.height * scalar)

	def __rmul__(self, scalar: float) -> Dim2:
		return Dim2(self.width * scalar, self.height * scalar)

	def __truediv__(self, scalar: float) -> Dim2:
		return Dim2(self.width / scalar, self.height / scalar)

	def __rtruediv__(self, scalar: float) -> Dim2:
		return Dim2(self.width / scalar, self.height / scalar)
