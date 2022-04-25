from __future__ import annotations
from typing import Any, TypeVar, Generic
from src.utils.dim2.Dim2 import Dim2
from abc import ABC, abstractmethod, abstractstaticmethod

T = TypeVar("T")


class Point2(ABC, Generic[T]):
	def __init__(self, x: T, y: T) -> None:
		self._x: T = x
		self._y: T = y

	@property
	def x(self) -> T:
		return self._x

	@property
	def y(self) -> T:
		return self._y

	@staticmethod
	@abstractmethod
	def fromDim2(dim: Dim2[T]) -> Point2[T]:
		pass

	@abstractmethod
	def __str__(self) -> str:
		pass

	@abstractmethod
	def __repr__(self) -> str:
		pass

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Point2):
			return False
		return self.x == other.x and self.y == other.y

	def __ne__(self, other: Any) -> bool:
		if not isinstance(other, Point2):
			return True
		return self.x != other.x or self.y != other.y

	@abstractmethod
	def __add__(self, other: Point2[T]) -> Point2[T]:
		pass

	@abstractmethod
	def __sub__(self, other: Point2) -> Point2[T]:
		pass

	@abstractmethod
	def __mul__(self, scalar: T) -> Point2[T]:
		pass

	@abstractmethod
	def __rmul__(self, scalar: T) -> Point2:
		pass

	@abstractmethod
	def __truediv__(self, scalar: float) -> Point2:
		pass

	@abstractmethod
	def __rtruediv__(self, scalar: float) -> Point2:
		pass

	@abstractmethod
	def multiplyComponents(self, other: Point2) -> Point2:
		pass

	@abstractmethod
	def dotProduct(self, other: Point2) -> float:
		pass
