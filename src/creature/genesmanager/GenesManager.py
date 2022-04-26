from __future__ import annotations
from src.creature.utils.gene.Gene import Gene
import random
from uuid import uuid4
from src.creature.genes.cells.body.BodyGene import BodyGene


class GenesManager:
	def __init__(
		self,
		genes: set[Gene],
	) -> None:
		self._genes: set[Gene] = genes

	@property
	def genes(self) -> frozenset[Gene]:
		return frozenset[Gene](self._genes)

	@staticmethod
	def generateRandom() -> GenesManager:
		genes: set[Gene] = set[Gene]()
		for _ in range(random.randint(1, 5)):
			genes.add(
				BodyGene(
					id=str(uuid4()),
					radius=random.uniform(5.0, 9.5),
				)
			)
		return GenesManager(genes)
