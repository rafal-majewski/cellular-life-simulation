from typing import Any
from src.utils.dim2.FloatDim2 import FloatDim2
from src.config.worldconfig.atomsconfig.AtomsConfig import AtomsConfig


class WorldConfig:
	def __init__(self, size: FloatDim2, atoms: AtomsConfig):
		self._size: FloatDim2 = size
		self._atoms: AtomsConfig = atoms

	@property
	def size(self) -> FloatDim2:
		return self._size

	@property
	def atoms(self) -> AtomsConfig:
		return self._atoms

	@staticmethod
	def fromJson(json: Any):
		return WorldConfig(
			size=FloatDim2.fromJson(json["size"]),
			atoms=AtomsConfig.fromJson(json["atoms"]),
		)
