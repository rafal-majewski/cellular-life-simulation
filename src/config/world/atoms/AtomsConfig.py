from __future__ import annotations
from typing import Any
from src.config.world.atoms.air.AirConfig import AirConfig
from src.config.world.atoms.cells.CellConfig import CellConfig


class AtomsConfig:
	def __init__(self, air: AirConfig, cells: CellConfig) -> None:
		self._air: AirConfig = air
		self._cells: CellConfig = cells

	@property
	def air(self) -> AirConfig:
		return self._air

	@property
	def cells(self) -> CellConfig:
		return self._cells

	@staticmethod
	def fromJson(json: Any) -> AtomsConfig:
		return AtomsConfig(
			air=AirConfig.fromJson(json["air"]),
			cells=CellConfig.fromJson(json["cells"]),
		)
