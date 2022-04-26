from __future__ import annotations
from typing import Any
from src.utils.color.Color import Color


class AirConfig:
	def __init__(self, radius: float, color: Color):
		self._radius: float = radius
		self._color: Color = color

	@property
	def radius(self) -> float:
		return self._radius

	@property
	def color(self) -> Color:
		return self._color

	@staticmethod
	def fromJson(json: Any) -> AirConfig:
		return AirConfig(
			radius=float(json["radius"]),
			color=Color.fromJson(json["color"]),
		)
