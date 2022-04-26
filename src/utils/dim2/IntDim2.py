from __future__ import annotations
from typing import Any
from src.utils.dim2.Dim2 import Dim2


class IntDim2(Dim2[int]):
	def __init__(self, width: int, height: int) -> None:
		self._width: int = width
		self._height: int = height

	@property
	def width(self) -> int:
		return self._width

	@property
	def height(self) -> int:
		return self._height

	def __repr__(self) -> str:
		return f"IntDim2({self.width}, {self.height})"

	def __str__(self) -> str:
		return f"IntDim2({self.width}, {self.height})"

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, IntDim2):
			return False
		return self.width == other.width and self.height == other.height

	def __add__(self, other: Dim2[int]) -> IntDim2:
		return IntDim2(self.width + other.width, self.height + other.height)

	def __sub__(self, other: Dim2[int]) -> IntDim2:
		return IntDim2(self.width - other.width, self.height - other.height)

	def __mul__(self, scalar: int) -> IntDim2:
		return IntDim2(self.width * scalar, self.height * scalar)

	def __rmul__(self, scalar: int) -> IntDim2:
		return IntDim2(self.width * scalar, self.height * scalar)

	def __truediv__(self, scalar: int) -> IntDim2:
		return IntDim2(int(self.width / scalar), int(self.height / scalar))

	def __rtruediv__(self, scalar: int) -> IntDim2:
		return IntDim2(int(self.width / scalar), int(self.height / scalar))
