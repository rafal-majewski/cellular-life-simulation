from src.utils.point2.FloatPoint2 import FloatPoint2
from src.utils.dim2.Dim2 import Dim2


class BoundingBox2:
	def __init__(self, center: FloatPoint2, size: Dim2) -> None:
		self._center: FloatPoint2 = center
		self._size: Dim2 = size

	@property
	def center(self) -> FloatPoint2:
		return self._center

	@property
	def size(self) -> Dim2:
		return self._size

	@property
	def topLeft(self) -> FloatPoint2:
		return self._center \
			+ FloatPoint2.fromDim2(self._size).multiplyComponents(FloatPoint2(-0.5, -0.5))

	@property
	def bottomRight(self) -> FloatPoint2:
		return self._center \
			+ FloatPoint2.fromDim2(self._size).multiplyComponents(FloatPoint2(0.5, 0.5))

	@property
	def topRight(self) -> FloatPoint2:
		return self._center \
			+ FloatPoint2.fromDim2(self._size).multiplyComponents(FloatPoint2(0.5, -0.5))

	@property
	def bottomLeft(self) -> FloatPoint2:
		return self._center \
			+ FloatPoint2.fromDim2(self._size).multiplyComponents(FloatPoint2(-0.5, 0.5))
