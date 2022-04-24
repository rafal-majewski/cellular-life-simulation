class Quadtree:
	def __init__(self, *, minChunkSize: float, maxChunkSize: float) -> None:
		self._minChunkSize: float = minChunkSize
		self._maxChunkSize: float = maxChunkSize

	@property
	def minChunkSize(self) -> float:
		return self._minChunkSize

	@property
	def maxChunkSize(self) -> float:
		return self._maxChunkSize
