from typing import Any
from src.config.gameconfig.worldconfig.WorldConfig import WorldConfig


class GameConfig:
	def __init__(
		self,
		*,
		world: WorldConfig,
		fps: float,
	) -> None:
		self._world: WorldConfig = world
		self._fps: float = fps

	@property
	def world(self) -> WorldConfig:
		return self._world

	@property
	def fps(self) -> float:
		return self._fps

	@staticmethod
	def fromJson(json: Any):
		return GameConfig(
			world=WorldConfig.fromJson(json["world"]),
			fps=float(json["fps"]),
		)
