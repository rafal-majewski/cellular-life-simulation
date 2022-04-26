import random
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.world.atoms.cell.Cell import Cell
from src.world.physics.utils.joint.Joint import Joint
from src.creature.utils.gene.cell.CellGene import CellGene
from src.creature.genes.cells.body.BodyGene import BodyGene
from src.utils.color.Color import Color


class CreatureSpawner:
	def __init__(self) -> None:
		self._cells: dict[str, Cell] = dict[str, Cell]()
		self._joints: dict[str, Joint] = dict[str, Joint]()

	def createCell(
		self,
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

	def applyBodyGene(self, bodyGene: BodyGene) -> None:
		cell: Cell = self.createCell(
			radius=bodyGene.radius,
			color=Color(0, 255, 0)
		)
		self._cells[bodyGene.id] = cell


			

	def applyCellGene(self, cellGene: CellGene) -> None:
		if isinstance(cellGene, BodyGene):
			self.applyBodyGene(cellGene)