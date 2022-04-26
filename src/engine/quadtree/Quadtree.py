from typing import Optional
from src.engine.utils.atom.Atom import Atom
from src.engine.quadtree.Chunk import Chunk
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.utils.point2.IntPoint2 import IntPoint2
from src.utils.dim2.FloatDim2 import FloatDim2
from src.engine.utils.boundingbox2.BoundingBox2 import BoundingBox2

# TODO:
# write a better implementation

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
		self._chunksByAtom: dict[Atom, set[Chunk]] = dict[Atom, set[Chunk]]()

	@property
	def minChunkSize(self) -> FloatDim2:
		return self._minChunkSize

	def assertAtomFits(self, atom: Atom) -> None:
		if atom.boundingBox.size.width > self._maxChunkSize.width \
			or atom.boundingBox.size.height > self._maxChunkSize.height:
			raise ValueError(
				"Atom does not fit"
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

	def _addAtomByPoint(self, atom: Atom, point: FloatPoint2) -> None:
		chunkPosition: IntPoint2 = IntPoint2.fromPoint2(
			(point + FloatPoint2.fromDim2(self._maxChunkSize / 2))
			.divideComponents(FloatPoint2.fromDim2(self._maxChunkSize))
			.floor()
		)
		chunk: Chunk = self._getOrCreateGetChunk(chunkPosition)
		self._chunksByAtom[atom].add(chunk)
		chunk.addAtomByPoint(atom, point)

	def addAtom(self, atom: Atom) -> None:
		self.assertAtomFits(atom)
		self._chunksByAtom[atom] = set[Chunk]()
		self._addAtomByPoint(atom, atom.boundingBox.topLeft)
		self._addAtomByPoint(atom, atom.boundingBox.topRight)
		self._addAtomByPoint(atom, atom.boundingBox.bottomLeft)
		self._addAtomByPoint(atom, atom.boundingBox.bottomRight)

	def removeAtom(self, atom: Atom) -> None:
		for chunk in self._chunksByAtom[atom]:
			chunk.removeAtom(atom)
			if chunk.isEmpty():
				chunkPosition: IntPoint2 = IntPoint2.fromPoint2(
						chunk.realPosition.divideComponents(
						FloatPoint2.fromDim2(self._maxChunkSize)
					).floor()
				)
				del self._mainChunks[chunkPosition.y][chunkPosition.x]
				if len(self._mainChunks[chunkPosition.y]) == 0:
					del self._mainChunks[chunkPosition.y]
		del self._chunksByAtom[atom]

	def _getNeighborsByPoint(self, point: FloatPoint2, acc: set[Atom]) -> None:
		chunkPosition: IntPoint2 = IntPoint2.fromPoint2(
			(point + FloatPoint2.fromDim2(self._maxChunkSize / 2))
			.divideComponents(FloatPoint2.fromDim2(self._maxChunkSize))
			.floor()
		)
		chunk: Optional[Chunk] = self._getChunk(chunkPosition)
		if chunk is not None:
			for atom in chunk._atoms:
				acc.add(atom)

	def getNeighbors(self, atom: Atom) -> set[Atom]:
		boundingBox: BoundingBox2 = atom.boundingBox
		# assert
		neighbors: set[Atom] = set[Atom]()
		self._getNeighborsByPoint(boundingBox.topLeft, neighbors)
		self._getNeighborsByPoint(boundingBox.topRight, neighbors)
		self._getNeighborsByPoint(boundingBox.bottomLeft, neighbors)
		self._getNeighborsByPoint(boundingBox.bottomRight, neighbors)
		return neighbors