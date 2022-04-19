from src.engine.Cell import Cell


class World:
	def __init__(self) -> None:
		self.cells = set[Cell]()

	def addCell(self, cell: Cell) -> None:
		self.cells.add(cell)

	def testCellCellCollision(self, cell1: Cell, cell2: Cell) -> bool:
		return \
			(cell1.position - cell2.position).magnitude \
			< cell1.radius + cell2.radius

	def cellCellCollision(self, cell1: Cell, cell2: Cell) -> None:
		pass

	def resolveCellCellCollision(self, cell1: Cell, cell2: Cell) -> None:
		if not self.testCellCellCollision(cell1, cell2):
			return
		self.cellCellCollision(cell1, cell2)

	def resolveCollisions(self) -> None:
		for cell1 in self.cells:
			for cell2 in self.cells:
				self.cellCellCollision(cell1, cell2)

	def tick(self, deltaTime: float) -> None:
		self.resolveCollisions()
		for cell in self.cells:
			cell.position += cell.velocity * deltaTime
