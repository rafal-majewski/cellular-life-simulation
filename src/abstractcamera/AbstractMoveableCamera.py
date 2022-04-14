from src.abstractcamera.AbstractCamera import AbstractCamera
from src.utils.Point2 import Point2


class AbstractMoveableCamera(AbstractCamera):
	def __init__(self, *, position: Point2) -> None:
		super().__init__()
		self.position = position

	@property
	def position(self) -> Point2:
		return self._position

	@position.setter
	def position(self, position: Point2) -> None:
		self._position = position
