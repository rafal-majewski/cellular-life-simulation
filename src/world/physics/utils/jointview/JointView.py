# Wrapper class for preventing direct modification of
# joint

from src.world.physics.utils.atomview.AtomView import AtomView
from src.world.physics.utils.joint.Joint import Joint


class JointView:
	def __init__(self, joint: Joint) -> None:
		self._joint: Joint = joint
		self._atom1: AtomView = AtomView(joint.atom1)
		self._atom2: AtomView = AtomView(joint.atom2)

	@property
	def atom1(self) -> AtomView:
		return self._atom1

	@property
	def atom2(self) -> AtomView:
		return self._atom2

	@property
	def restDistance(self) -> float:
		return self._joint.restDistance

	@property
	def stiffness(self) -> float:
		return self._joint.stiffness

	def __str__(self) -> str:
		return (
			f"JointView("
			f"joint={self._joint}, "
			f"atom1={self.atom1}, "
			f"atom2={self.atom2}"
			f")"
		)
