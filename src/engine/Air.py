from src.engine.Cell import Cell
from src.utils.Point2 import Point2


class Air(Cell):
	def __init__(
		self,
		*,
		position: Point2,
		velocity: Point2 = None,
	) -> None:
		super().__init__(
			position=position,
			velocity=velocity,
			mass=0.1,
			radius=10,
		)

	def __str__(self) -> str:
		return (
			f"Air("
			f"position={self.position}, "
			f"velocity={self.velocity}"
			f")"
		)
