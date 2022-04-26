from typing import Any


class GameConfig:
	def __init__(
		self,
		*,
		fps: float,
	) -> None:
		self._fps: float = fps

	@property
	def fps(self) -> float:
		return self._fps

	@staticmethod
	def fromJson(json: Any):
		return GameConfig(
			fps=float(json["fps"]),
		)
