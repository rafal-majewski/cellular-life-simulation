from src.abstractcamera.AbstractCamera import AbstractCamera
from src.utils.point2.FloatPoint2 import FloatPoint2


class AbstractMoveableCamera(AbstractCamera):
	def __init__(self, *, position: FloatPoint2) -> None:
		super().__init__()
		self.position = position

	@property
	def position(self) -> FloatPoint2:
		return self._position

	@position.setter
	def position(self, position: FloatPoint2) -> None:
		self._position = position
