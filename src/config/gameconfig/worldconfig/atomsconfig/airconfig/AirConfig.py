from __future__ import annotations
from typing import Any
from src.utils.color.Color import Color


class AirConfig:
	def __init__(
		self,
		*,
		radius: float,
		color: Color,
		mass: float,
	) -> None:
		self._radius: float = radius
		self._color: Color = color
		self._mass: float = mass

	@property
	def radius(self) -> float:
		return self._radius

	@property
	def color(self) -> Color:
		return self._color

	@property
	def mass(self) -> float:
		return self._mass

	@staticmethod
	def fromJson(json: Any) -> AirConfig:
		return AirConfig(
			radius=float(json["radius"]),
			color=Color.fromJson(json["color"]),
			mass=float(json["mass"]),
		)
