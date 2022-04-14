from src.engine import Cell


class World:
	def __init__(self) -> None:
		self.cells = set[Cell]()

	def addCell(self, cell: Cell) -> None:
		self.cells.add(cell)

	def tick(self, deltaTime: float) -> None:
		for cell in self.cells:
			cell.position += cell.velocity * deltaTime
