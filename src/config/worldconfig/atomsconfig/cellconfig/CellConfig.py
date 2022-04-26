from __future__ import annotations
from typing import Any
from src.utils.color.Color import Color


class CellConfig:
	def __init__(self, scale: float):
		self._scale: float = scale

	@property
	def scale(self) -> float:
		return self._scale

	@staticmethod
	def fromJson(json: Any) -> CellConfig:
		return CellConfig(
			scale=float(json["scale"]),
		)
