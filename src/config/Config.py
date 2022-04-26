from typing import Any
from src.config.gameconfig.GameConfig import GameConfig


class Config:
	def __init__(
		self,
		*,
		game: GameConfig,
	) -> None:
		self._game: GameConfig = game

	@property
	def game(self) -> GameConfig:
		return self._game

	@staticmethod
	def fromJson(json: Any):
		return Config(
			game=GameConfig.fromJson(json["game"])
		)
