class Dim2:
	def __init__(self, width: float, height: float) -> None:
		self._width: float = width
		self._height: float = height

	@property
	def width(self) -> float:
		return self._width

	@property
	def height(self) -> float:
		return self._height

	def __repr__(self) -> str:
		return f"Dim2({self.width}, {self.height})"

	def __str__(self) -> str:
		return f"Dim2({self.width}, {self.height})"

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Dim2):
			return False
		return self.width == other.width and self.height == other.height
