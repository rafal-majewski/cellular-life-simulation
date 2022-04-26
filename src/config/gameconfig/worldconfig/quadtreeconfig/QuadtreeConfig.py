from __future__ import annotations
from typing import Any
from src.config.gameconfig.worldconfig.quadtreeconfig.chunksconfig.ChunksConfig import ChunksConfig


class QuadtreeConfig:
	def __init__(
		self,
		*,
		chunks: ChunksConfig,
	) -> None:
		self._chunks: ChunksConfig = chunks

	@property
	def chunks(self) -> ChunksConfig:
		return self._chunks

	@staticmethod
	def fromJson(json: Any) -> QuadtreeConfig:
		return QuadtreeConfig(
			chunks=ChunksConfig.fromJson(json["chunks"]),
		)
