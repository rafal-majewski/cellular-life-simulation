from src.engine.Cell import Cell


class Joint:
	def __init__(
		self,
		*,
		cell1: Cell,
		cell2: Cell,
		stiffness: float,
	) -> None:
		self.cell1: Cell = cell1
		self.cell2: Cell = cell2
		self.stiffness: float = stiffness

	@property
	def restDistance(self) -> float:
		return self.cell1.radius + self.cell2.radius

	def __str__(self) -> str:
		return f"Joint(cell1={self.cell1}, cell2={self.cell2}, stiffness={self.stiffness})"
