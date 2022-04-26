from typing import Any
from src.utils.dim2.IntDim2 import IntDim2


class WindowConfig:
	def __init__(
		self,
		*,
		size: IntDim2
	) -> None:
		self._size: IntDim2 = size

	@property
	def size(self) -> IntDim2:
		return self._size

	@staticmethod
	def fromJson(json: Any):
		return WindowConfig(
			size=IntDim2.fromJson(json["size"]),
		)
