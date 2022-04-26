from __future__ import annotations
from typing import Any
from src.utils.dim2.Dim2 import Dim2


class FloatDim2(Dim2[float]):
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
		return f"FloatDim2({self.width}, {self.height})"

	def __str__(self) -> str:
		return f"FloatDim2({self.width}, {self.height})"

	def __add__(self, other: Dim2[float]) -> FloatDim2:
		return FloatDim2(self.width + other.width, self.height + other.height)

	def __sub__(self, other: Dim2[float]) -> FloatDim2:
		return FloatDim2(self.width - other.width, self.height - other.height)

	def __mul__(self, scalar: float) -> FloatDim2:
		return FloatDim2(self.width * scalar, self.height * scalar)

	def __rmul__(self, scalar: float) -> FloatDim2:
		return FloatDim2(self.width * scalar, self.height * scalar)

	def __truediv__(self, scalar: float) -> FloatDim2:
		return FloatDim2(self.width / scalar, self.height / scalar)

	def __rtruediv__(self, scalar: float) -> FloatDim2:
		return FloatDim2(self.width / scalar, self.height / scalar)

	@staticmethod
	def fromJson(json: Any) -> FloatDim2:
		return FloatDim2(json["width"], json["height"])
