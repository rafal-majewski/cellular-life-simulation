from src.creature.gene.Gene import Gene


class Creature:
	def __init__(self) -> None:
		self.genes: set[Gene] = set[Gene]()
