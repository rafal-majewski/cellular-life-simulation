from src.engine.physics.JointView import JointView
from src.utils.point2.FloatPoint2 import FloatPoint2


class JointResolver:
	def resolve(self, jointView: JointView) -> None:
		dir1: FloatPoint2 = \
			(jointView.cell2.position - jointView.cell1.position).normalize()
		dir2: FloatPoint2 = \
			(jointView.cell1.position - jointView.cell2.position).normalize()
		missingDist: float = \
			(jointView.cell2.position - jointView.cell1.position).magnitude \
			- jointView.restDistance
		mag1: float = \
			missingDist * jointView.cell1.mass \
			/ (jointView.cell1.mass + jointView.cell2.mass)
		mag2: float = \
			missingDist * jointView.cell2.mass \
			/ (jointView.cell1.mass + jointView.cell2.mass)
		jointView.cell1.velocity += mag1 * dir1 * jointView.stiffness
		jointView.cell2.velocity += mag2 * dir2 * jointView.stiffness
