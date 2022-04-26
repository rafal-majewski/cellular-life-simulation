from src.engine.physics.utils.atomview.AtomView import AtomView
from src.utils.point2.FloatPoint2 import FloatPoint2


class CollisionResolver:
	def test(self, atomView1: AtomView, atomView2: AtomView) -> bool:
		return \
			(atomView1.position - atomView2.position).magnitude \
			< atomView1.radius + atomView2.radius

	def collision(self, atomView1: AtomView, atomView2: AtomView) -> None:
		# print("atomAtomCollision")
		# https://en.wikipedia.org/wiki/Elastic_collision

		# check if the atoms should bounce
		if (atomView1.velocity - atomView2.velocity) \
			.dotProduct(atomView1.position - atomView2.position) >= 0:
			return

		distance: float = (atomView1.position - atomView2.position).magnitude

		newVelocity1: FloatPoint2 = \
			atomView1.velocity \
			- 2 * atomView2.mass / (atomView1.mass + atomView2.mass) \
			* (
				(atomView1.velocity - atomView2.velocity)
				.dotProduct(atomView1.position - atomView2.position)
			) \
			/ (distance ** 2) \
			* (atomView1.position - atomView2.position)
		newVelocity2: FloatPoint2 = \
			atomView2.velocity \
			- 2 * atomView1.mass / (atomView1.mass + atomView2.mass) \
			* (
				(atomView2.velocity - atomView1.velocity)
				.dotProduct(atomView2.position - atomView1.position)
			) \
			/ (distance ** 2) \
			* (atomView2.position - atomView1.position)

		atomView1.velocity = newVelocity1
		atomView2.velocity = newVelocity2

	def resolve(self, deltaTime: float, atomView1: AtomView, atomView2: AtomView) -> None:
		if not self.test(atomView1, atomView2):
			return
		self.collision(atomView1, atomView2)
