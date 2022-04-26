from abc import ABC
from typing import Optional
from src.utils.point2.FloatPoint2 import FloatPoint2


class Movable(ABC):
	def __init__(
		self,
		*,
		position: FloatPoint2,
		velocity: Optional[FloatPoint2] = None,
	) -> None:
		self.position: FloatPoint2 = position
		self.velocity: FloatPoint2 = \
			FloatPoint2(0, 0) if velocity is None else velocity
	