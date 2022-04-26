from __future__ import annotations
from typing import Any
from src.config.worldconfig.atomsconfig.airconfig.AirConfig import AirConfig
from src.config.worldconfig.atomsconfig.cellconfig.CellConfig import CellConfig


class AtomsConfig:
	def __init__(self, air: AirConfig, cell: CellConfig):
		self._air: AirConfig = air
		self._cell: CellConfig = cell

	@staticmethod
	def fromJson(json: Any) -> AtomsConfig:
		return AtomsConfig(
			air=AirConfig.fromJson(json["air"]),
			cell=CellConfig.fromJson(json["cell"]),
		)
