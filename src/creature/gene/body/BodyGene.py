from src.creature.gene.Gene import Gene
import random


class BodyGene(Gene):
	def __init__(self, radius: float) -> None:
		super().__init__()
		self._radius = radius

	@property
	def radius(self) -> float:
		return self._radius

	def mutate(self, rate: float) -> None:
		self._radius += self._radius * rate * random.uniform(-1, 1)

	def __str__(self) -> str:
		return f"BodyGene(radius={self.radius})"
