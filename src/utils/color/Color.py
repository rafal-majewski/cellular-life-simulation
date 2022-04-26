from __future__ import annotations
from typing import Any


class Color:
	def __init__(self, r: int, g: int, b: int) -> None:
		self.r = r
		self.g = g
		self.b = b

	@staticmethod
	def fromJson(json: Any) -> Color:
		return Color(
			r=int(json["r"]),
			g=int(json["g"]),
			b=int(json["b"]),
		)

	def __str__(self) -> str:
		return f"Color(r={self.r}, g={self.g}, b={self.b})"
