from src.engine.Cell import Cell


class Joint:
	def __init__(
		self,
		*,
		cell1: Cell,
		cell2: Cell,
		stiffness: float,
	) -> None:
		self.cell1 = cell1
		self.cell2 = cell2
		self.stiffness = stiffness
