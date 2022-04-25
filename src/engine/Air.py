from src.engine.Cell import Cell
from src.utils.point2.FloatPoint2 import FloatPoint2


class Air(Cell):
	def __init__(
		self,
		*,
		position: FloatPoint2,
		velocity: FloatPoint2 = None,
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
