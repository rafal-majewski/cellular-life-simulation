class Chunk:
	def __init__(self, *, size: float) -> None:
		self._size: float = size

	@property
	def size(self) -> float:
		return self._size
