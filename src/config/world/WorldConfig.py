from typing import Any
from src.utils.dim2.FloatDim2 import FloatDim2
from src.config.world.atoms.AtomsConfig import AtomsConfig
from src.config.world.quadtree.QuadtreeConfig import QuadtreeConfig


class WorldConfig:
	def __init__(
		self,
		*,
		size:FloatDim2,
		atoms: AtomsConfig,
		quadtree: QuadtreeConfig,
	) -> None:
		self._size: FloatDim2 = size
		self._atoms: AtomsConfig = atoms
		self._quadtree: QuadtreeConfig = quadtree

	@property
	def size(self) -> FloatDim2:
		return self._size

	@property
	def atoms(self) -> AtomsConfig:
		return self._atoms

	@property
	def quadtree(self) -> QuadtreeConfig:
		return self._quadtree

	@staticmethod
	def fromJson(json: Any):
		return WorldConfig(
			size=FloatDim2.fromJson(json["size"]),
			atoms=AtomsConfig.fromJson(json["atoms"]),
			quadtree=QuadtreeConfig.fromJson(json["quadtree"]),
		)
