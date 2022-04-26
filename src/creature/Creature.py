from __future__ import annotations
from src.creature.gene.Gene import Gene


class Creature:
	def __init__(self) -> None:
		self._genes: set[Gene] = set[Gene]()

	@staticmethod
	def generate() -> Creature:
		creature = Creature()
		return creature
