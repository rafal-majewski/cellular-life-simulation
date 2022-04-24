from src.utils.Point2 import Point2
from src.utils.Dim2 import Dim2


class BoundingBox2:
	def __init__(self, center: Point2, size: Dim2) -> None:
		self._center: Point2 = center
		self._size: Dim2 = size

	@property
	def center(self) -> Point2:
		return self._center

	@property
	def size(self) -> Dim2:
		return self._size

	@property
	def topLeft(self) -> Point2:
		return self._center \
			+ Point2.fromDim2(self._size).multiplyComponents(Point2(-0.5, -0.5))

	@property
	def bottomRight(self) -> Point2:
		return self._center \
			+ Point2.fromDim2(self._size).multiplyComponents(Point2(0.5, 0.5))

	@property
	def topRight(self) -> Point2:
		return self._center \
			+ Point2.fromDim2(self._size).multiplyComponents(Point2(0.5, -0.5))

	@property
	def bottomLeft(self) -> Point2:
		return self._center \
			+ Point2.fromDim2(self._size).multiplyComponents(Point2(-0.5, 0.5))
