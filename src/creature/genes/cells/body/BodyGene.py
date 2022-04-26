from src.creature.utils.gene.cell.CellGene import CellGene
import random


class BodyGene(CellGene):
	def __init__(self, id: str, radius: float) -> None:
		super().__init__(id=id)
		self._radius = radius

	@property
	def radius(self) -> float:
		return self._radius

	def mutate(self, rate: float) -> None:
		self._radius += self._radius * rate * random.uniform(-1, 1)

	def __str__(self) -> str:
		return f"BodyGene(radius={self.radius})"
