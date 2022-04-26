from __future__ import annotations
from src.creature.genesmanager.GenesManager import GenesManager
from src.world.atoms.cell.Cell import Cell
from src.world.physics.utils.joint.Joint import Joint


class Creature:
	def __init__(
		self,
		*,
		genesManager: GenesManager,
		cells: set[Cell],
		joints: set[Joint],
	) -> None:
		self._genesManager: GenesManager = genesManager
		self._cells: set[Cell] = cells
		self._joints: set[Joint] = joints

	@property
	def genesManager(self) -> GenesManager:
		return self._genesManager

	@property
	def cells(self) -> frozenset[Cell]:
		return frozenset[Cell](self._cells)

	@property
	def joints(self) -> frozenset[Joint]:
		return frozenset[Joint](self._joints)

	# @staticmethod
	# def generateGenes() -> set[Gene]:
	# 	genes: set[Gene] = set[Gene]()
	# 	for _ in range(random.randint(1, 5)):
	# 		genes.add(
	# 			BodyGene(
	# 				id=str(uuid4()),
	# 				radius=random.uniform(0.1, 0.5),
	# 			)
	# 		)
	# 	return genes

	# @staticmethod
	# def generate() -> Creature:
	# 	creature: Creature = Creature(Creature.generateGenes())
	# 	return creature

	def __str__(self) -> str:
		return f'Creature(genesManager={self.genesManager}, cells={self._cells}, joints={self._joints})'
