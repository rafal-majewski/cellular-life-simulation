from src.engine.physics.utils.jointview.JointView import JointView
from src.utils.point2.FloatPoint2 import FloatPoint2


class JointResolver:
	def resolve(self, deltaTime: float, jointView: JointView) -> None:
		# todo:
		# the function violates the law of conservation of energy
		dir1: FloatPoint2 = \
			(jointView.atom2.position - jointView.atom1.position).normalize()
		dir2: FloatPoint2 = \
			(jointView.atom1.position - jointView.atom2.position).normalize()
		missingDist: float = \
			(jointView.atom2.position - jointView.atom1.position).magnitude \
			- jointView.restDistance
		mag1: float = \
			missingDist * jointView.atom1.mass \
			/ (jointView.atom1.mass + jointView.atom2.mass)
		mag2: float = \
			missingDist * jointView.atom2.mass \
			/ (jointView.atom1.mass + jointView.atom2.mass)
		jointView.atom1.velocity += mag1 * dir1 * jointView.stiffness
		jointView.atom2.velocity += mag2 * dir2 * jointView.stiffness
