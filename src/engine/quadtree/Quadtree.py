from numbers import Integral
from src.engine.Cell import Cell
from src.engine.quadtree.Chunk import Chunk
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.utils.point2.IntPoint2 import IntPoint2


class Quadtree:
	def __init__(self, *, minChunkSize: float, maxChunkSize: float) -> None:
		self._minChunkSize: float = minChunkSize
		self._maxChunkSize: float = maxChunkSize
		self._chunks: dict[int, dict[int, Chunk]] = dict[int, dict[int, Chunk]]()

	@property
	def minChunkSize(self) -> float:
		return self._minChunkSize

	def assertCellFits(self, cell: Cell) -> None:
		if cell.boundingBox.size.width > self._maxChunkSize \
			or cell.boundingBox.size.height > self._maxChunkSize:
			raise ValueError(
				f"Cell is too big to fit in a quadtree: {cell.boundingBox}"
			)

	@property
	def maxChunkSize(self) -> float:
		return self._maxChunkSize

	# def _getOrGetCreateChunk(self, chunkPosition: IntPoint2) -> Chunk:
	# 	if chunkPosition.y not in self._chunks:
	# 		self._chunks[chunkPosition.y] = dict[int, Chunk]()
	# 	pass
		# if chunkPosition.x not in self._chunks:
		# 	self._chunks[chunkPosition.x] = dict[int, Chunk]()
		# if chunkPosition.y not in self._chunks[chunkPosition.x]:
		# 	self._chunks[chunkPosition.x][chunkPosition.y] =\
		# 		Chunk(size=self._minChunkSize)
		# return self._chunks[chunkPosition.x][chunkPosition.y]

	# def _addCellByPoint(self, cell: Cell, point: Point2) -> None:
	# 	chunk: Chunk = self._chunks[point.x][point.y]
	# 	chunk.addCell(cell)

	# def addCell(self,
