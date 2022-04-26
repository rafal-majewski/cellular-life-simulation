from typing import Optional
from src.engine.Cell import Cell
from src.engine.quadtree.Chunk import Chunk
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.utils.point2.IntPoint2 import IntPoint2
from src.utils.dim2.FloatDim2 import FloatDim2
from src.engine.BoundingBox2 import BoundingBox2



class Quadtree:
	def assertValidChunkSizeBoundaries(
		self,
		minChunkSize: FloatDim2,
		maxChunkSize: FloatDim2,
	) -> None:
		if minChunkSize.width > maxChunkSize.width \
			or minChunkSize.height > maxChunkSize.height:
			raise ValueError(
				"Min chunk size must be smaller than max chunk size"
			)

	def __init__(
		self,
		*,
		minChunkSize: FloatDim2,
		maxChunkSize: FloatDim2
	) -> None:
		self.assertValidChunkSizeBoundaries(minChunkSize, maxChunkSize)
		self._minChunkSize: FloatDim2 = minChunkSize
		self._maxChunkSize: FloatDim2 = maxChunkSize
		self._mainChunks: dict[int, dict[int, Chunk]] = dict[int, dict[int, Chunk]]()
		self._chunksByCell: dict[Cell, set[Chunk]] = dict[Cell, set[Chunk]]()

	@property
	def minChunkSize(self) -> FloatDim2:
		return self._minChunkSize

	def assertCellFits(self, cell: Cell) -> None:
		if cell.boundingBox.size.width > self._maxChunkSize.width \
			or cell.boundingBox.size.height > self._maxChunkSize.height:
			raise ValueError(
				"Cell does not fit"
			)

	@property
	def maxChunkSize(self) -> FloatDim2:
		return self._maxChunkSize

	def _createChunkIfDoesntExist(self, chunkPosition: IntPoint2) -> None:
		if chunkPosition.y not in self._mainChunks:
			self._mainChunks[chunkPosition.y] = dict[int, Chunk]()
		if chunkPosition.x not in self._mainChunks[chunkPosition.y]:
			realChunkPosition: FloatPoint2 = FloatPoint2.fromPoint2(
				chunkPosition
			).multiplyComponents(FloatPoint2.fromDim2(self._maxChunkSize))

			self._mainChunks[chunkPosition.y][chunkPosition.x] = Chunk.create(
				quadtree=self,
				realPosition=realChunkPosition,
				size=self._maxChunkSize,
			)

	def _getOrCreateGetChunk(self, chunkPosition: IntPoint2) -> Chunk:
		self._createChunkIfDoesntExist(chunkPosition)
		return self._mainChunks[chunkPosition.y][chunkPosition.x]

	def _getChunk(self, chunkPosition: IntPoint2) -> Optional[Chunk]:
		if chunkPosition.y in self._mainChunks:
			if chunkPosition.x in self._mainChunks[chunkPosition.y]:
				return self._mainChunks[chunkPosition.y][chunkPosition.x]
		return None

	def _addCellByPoint(self, cell: Cell, point: FloatPoint2) -> None:
		chunkPosition: IntPoint2 = IntPoint2.fromPoint2(
			(point + FloatPoint2.fromDim2(self._maxChunkSize / 2))
			.divideComponents(FloatPoint2.fromDim2(self._maxChunkSize))
			.floor()
		)
		chunk: Chunk = self._getOrCreateGetChunk(chunkPosition)
		self._chunksByCell[cell].add(chunk)
		chunk.addCellByPoint(cell, point)

	def addCell(self, cell: Cell) -> None:
		self.assertCellFits(cell)
		self._chunksByCell[cell] = set[Chunk]()
		self._addCellByPoint(cell, cell.boundingBox.topLeft)
		self._addCellByPoint(cell, cell.boundingBox.topRight)
		self._addCellByPoint(cell, cell.boundingBox.bottomLeft)
		self._addCellByPoint(cell, cell.boundingBox.bottomRight)

	def removeCell(self, cell: Cell) -> None:
		for chunk in self._chunksByCell[cell]:
			chunk.removeCell(cell)
			if chunk.isEmpty():
				chunkPosition: IntPoint2 = IntPoint2.fromPoint2(
						chunk.realPosition.divideComponents(
						FloatPoint2.fromDim2(self._maxChunkSize)
					).floor()
				)
				del self._mainChunks[chunkPosition.y][chunkPosition.x]
				if len(self._mainChunks[chunkPosition.y]) == 0:
					del self._mainChunks[chunkPosition.y]
		del self._chunksByCell[cell]

	def _getNeighborsByPoint(self, point: FloatPoint2, acc: set[Cell]) -> None:
		chunkPosition: IntPoint2 = IntPoint2.fromPoint2(
			(point + FloatPoint2.fromDim2(self._maxChunkSize / 2))
			.divideComponents(FloatPoint2.fromDim2(self._maxChunkSize))
			.floor()
		)
		chunk: Optional[Chunk] = self._getChunk(chunkPosition)
		if chunk is not None:
			for cell in chunk._cells:
				acc.add(cell)

	def getNeighbors(self, boundingBox: BoundingBox2) -> set[Cell]:
		# assert
		neighbors: set[Cell] = set[Cell]()
		self._getNeighborsByPoint(boundingBox.topLeft, neighbors)
		self._getNeighborsByPoint(boundingBox.topRight, neighbors)
		self._getNeighborsByPoint(boundingBox.bottomLeft, neighbors)
		self._getNeighborsByPoint(boundingBox.bottomRight, neighbors)
		return neighbors