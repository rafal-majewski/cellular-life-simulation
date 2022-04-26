from __future__ import annotations
from typing import Any, TypeVar, Generic
from abc import ABC, abstractmethod


T = TypeVar("T")


class Dim2(ABC, Generic[T]):
	def __init__(self, width: T, height: T) -> None:
		self._width: T = width
		self._height: T = height

	@property
	def width(self) -> T:
		return self._width

	@property
	def height(self) -> T:
		return self._height

	@abstractmethod
	def __repr__(self) -> str:
		pass

	@abstractmethod
	def __str__(self) -> str:
		pass

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Dim2):
			return False
		return self.width == other.width and self.height == other.height

	@abstractmethod
	def __add__(self, other: Dim2) -> Dim2:
		pass

	@abstractmethod
	def __sub__(self, other: Dim2) -> Dim2:
		pass

	@abstractmethod
	def __mul__(self, scalar: T) -> Dim2:
		pass

	@abstractmethod
	def __rmul__(self, scalar: T) -> Dim2:
		pass

	@abstractmethod
	def __truediv__(self, scalar: T) -> Dim2:
		pass

	@abstractmethod
	def __rtruediv__(self, scalar: T) -> Dim2:
		pass
