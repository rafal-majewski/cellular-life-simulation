# Wrapper class for preventing direct modification of
# joint

from src.engine.physics.CellView import CellView
from src.engine.Joint import Joint


class JointView:
	def __init__(self, joint: Joint) -> None:
		self._joint: Joint = joint
		self._cell1: CellView = CellView(joint.cell1)
		self._cell2: CellView = CellView(joint.cell2)

	@property
	def cell1(self) -> CellView:
		return self._cell1

	@property
	def cell2(self) -> CellView:
		return self._cell2

	@property
	def restDistance(self) -> float:
		return self._joint.restDistance

	@property
	def stiffness(self) -> float:
		return self._joint.stiffness

	def __str__(self) -> str:
		return f"JointView(joint={self._joint}, cell1={self.cell1}, cell2={self.cell2})"
