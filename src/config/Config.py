from typing import Any
from src.config.game.GameConfig import GameConfig
from src.config.window.WindowConfig import WindowConfig
from src.config.world.WorldConfig import WorldConfig


class Config:
	def __init__(
		self,
		*,
		game: GameConfig,
		window: WindowConfig,
		world: WorldConfig,
	) -> None:
		self._game: GameConfig = game
		self._window: WindowConfig = window
		self._world: WorldConfig = world

	@property
	def world(self) -> WorldConfig:
		return self._world

	@property
	def game(self) -> GameConfig:
		return self._game

	@property
	def window(self) -> WindowConfig:
		return self._window

	@staticmethod
	def fromJson(json: Any):
		return Config(
			game=GameConfig.fromJson(json["game"]),
			world=WorldConfig.fromJson(json["world"]),
			window=WindowConfig.fromJson(json["window"]),
		)
