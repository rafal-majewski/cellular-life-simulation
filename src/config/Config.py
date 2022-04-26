from typing import Any
from src.config.worldconfig.WorldConfig import WorldConfig


class Config:
	def __init__(self, world: WorldConfig):
		self._world: WorldConfig = world

	@property
	def world(self) -> WorldConfig:
		return self._world

	@staticmethod
	def fromJson(json: Any):
		return Config(
			world=WorldConfig.fromJson(json["world"])
		)
