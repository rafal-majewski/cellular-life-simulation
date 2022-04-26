import random
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.world.atoms.cell.Cell import Cell
from src.world.physics.utils.joint.Joint import Joint
from src.creature.utils.gene.cell.CellGene import CellGene
from src.creature.genes.cells.body.BodyGene import BodyGene
from src.utils.color.Color import Color
from src.creature.Creature import Creature
from src.creature.genesmanager.GenesManager import GenesManager
from src.world.atoms.cell.Cell import Cell
from src.world.physics.utils.joint.Joint import Joint
from src.creature.utils.gene.Gene import Gene



class CreatureBuilder:
	def __init__(self) -> None:
		self._cells: dict[str, Cell] = dict[str, Cell]()
		self._joints: set[Joint] = set[Joint]()

	@staticmethod
	def createCell(
		*,
		radius: float,
		color: Color,
	) -> Cell:
		cell = Cell(
			position=FloatPoint2(
				random.uniform(-1, 1),
				random.uniform(-1, 1),
			),
			mass=1,
			radius=radius,
			color=color
		)
		return cell

	@property
	def cells(self) -> set[Cell]:
		return set[Cell](self._cells.values())

	@property
	def joints(self) -> set[Joint]:
		return self._joints

	def applyBodyGene(self, bodyGene: BodyGene) -> None:
		cell: Cell = self.createCell(
			radius=bodyGene.radius,
			color=Color(0, 255, 0)
		)
		self._cells[bodyGene.id] = cell

	def applyCellGene(self, cellGene: CellGene) -> None:
		if isinstance(cellGene, BodyGene):
			self.applyBodyGene(cellGene)

	def applyGene(self, gene: Gene) -> None:
		if isinstance(gene, CellGene):
			self.applyCellGene(gene)

	@staticmethod
	def build(genesManager: GenesManager) -> Creature:
		creatureBuilder: CreatureBuilder = CreatureBuilder()
		for gene in genesManager.genes:
			creatureBuilder.applyGene(gene)
		return Creature(
			genesManager=genesManager,
			cells=creatureBuilder.cells,
			joints=creatureBuilder.joints,
		)
		
