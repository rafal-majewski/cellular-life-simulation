from __future__ import annotations
from typing import Any
from src.utils.dim2.FloatDim2 import FloatDim2
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.engine.Cell import Cell
from abc import ABC, abstractmethod
# from src.engine.quadtree.NonFinalChunk import NonFinalChunk
# from src.engine.quadtree.FinalChunk import FinalChunk
# from src.engine.quadtree.Quadtree import Quadtree


class Chunk(ABC):
	def __init__(
		self,
		*,
		quadtree: Any,
		realPosition: FloatPoint2,
		size: FloatDim2
	) -> None:
		self._realPosition: FloatPoint2 = realPosition
		self._size: FloatDim2 = size
		self._cells: set[Cell] = set[Cell]()

	@property
	def size(self) -> FloatDim2:
		return self._size

	@property
	def realPosition(self) -> FloatPoint2:
		return self._realPosition

	@abstractmethod
	def addCellByPoint(self, cell: Cell, point: FloatPoint2) -> None:
		pass

	def removeCell(self, cell: Cell) -> None:
		self._cells.remove(cell)

	@abstractmethod
	def isEmpty(self) -> bool:
		pass

	@staticmethod
	def create(
		*,
		quadtree: Any,
		realPosition: FloatPoint2,
		size: FloatDim2,
	) -> Chunk:
		# if size / 2 < minSize:
		# 	return FinalChunk(
		# 		quadtree=quadtree,
		# 		realPosition=realPosition,
		# 		size=size
		# 	)
		return FinalChunk(
			quadtree=quadtree,
			realPosition=realPosition,
			size=size,
		)


class FinalChunk(Chunk):
	def __init__(
		self,
		*,
		quadtree: Any,
		realPosition: FloatPoint2,
		size: FloatDim2
	) -> None:
		super().__init__(
			quadtree=quadtree,
			realPosition=realPosition,
			size=size
		)

	def addCellByPoint(self, cell: Cell, point: FloatPoint2) -> None:
		self._cells.add(cell)

	def isEmpty(self) -> bool:
		return len(self._cells) == 0
