# Wrapper class for preventing direct modification of
# cell's position and velocity

from src.engine.Cell import Cell
from src.utils.Point2 import Point2
from src.utils.Dim2 import Dim2
from src.engine.BoundingBox2 import BoundingBox2


class CellView:
	def __init__(self, cell: Cell) -> None:
		self._cell: Cell = cell
		self._position: Point2 = cell.position
		self._velocity: Point2 = cell.velocity

	@property
	def position(self) -> Point2:
		return self._position

	@position.setter
	def position(self, position: Point2) -> None:
		self._position = position

	@property
	def velocity(self) -> Point2:
		return self._velocity

	@velocity.setter
	def velocity(self, velocity: Point2) -> None:
		self._velocity = velocity

	@property
	def mass(self) -> float:
		return self._cell.mass

	@property
	def radius(self) -> float:
		return self._cell.radius

	@property
	def boundingBox(self) -> BoundingBox2:
		return self._cell.boundingBox

	def __str__(self) -> str:
		return f"CellView(cell={self._cell}, position={self.position}, velocity={self.velocity})"