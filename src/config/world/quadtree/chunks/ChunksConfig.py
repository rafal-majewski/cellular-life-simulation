from __future__ import annotations
from typing import Any
from src.utils.dim2.FloatDim2 import FloatDim2


class ChunksConfig:
	def __init__(
		self,
		*,
		minSize: FloatDim2,
		maxSize: FloatDim2,
	) -> None:
		self._minSize: FloatDim2 = minSize
		self._maxSize: FloatDim2 = maxSize

	@property
	def minSize(self) -> FloatDim2:
		return self._minSize

	@property
	def maxSize(self) -> FloatDim2:
		return self._maxSize

	@staticmethod
	def fromJson(json: Any) -> ChunksConfig:
		return ChunksConfig(
			minSize=FloatDim2.fromJson(json["minSize"]),
			maxSize=FloatDim2.fromJson(json["maxSize"]),
		)
