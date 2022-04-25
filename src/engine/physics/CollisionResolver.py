from src.engine.physics.CellView import CellView
from src.utils.point2.FloatPoint2 import FloatPoint2


class CollisionResolver:
	def test(self, cellView1: CellView, cellView2: CellView) -> bool:
		return \
			(cellView1.position - cellView2.position).magnitude \
			< cellView1.radius + cellView2.radius

	def collision(self, cellView1: CellView, cellView2: CellView) -> None:
		# print("cellCellCollision")
		# https://en.wikipedia.org/wiki/Elastic_collision

		# check if the cells should bounce
		if (cellView1.velocity - cellView2.velocity) \
			.dotProduct(cellView1.position - cellView2.position) >= 0:
			return

		distance: float = (cellView1.position - cellView2.position).magnitude

		newVelocity1: FloatPoint2 = \
			cellView1.velocity \
			- 2 * cellView2.mass / (cellView1.mass + cellView2.mass) \
			* (
				(cellView1.velocity - cellView2.velocity)
				.dotProduct(cellView1.position - cellView2.position)
			) \
			/ (distance ** 2) \
			* (cellView1.position - cellView2.position)
		newVelocity2: FloatPoint2 = \
			cellView2.velocity \
			- 2 * cellView1.mass / (cellView1.mass + cellView2.mass) \
			* (
				(cellView2.velocity - cellView1.velocity)
				.dotProduct(cellView2.position - cellView1.position)
			) \
			/ (distance ** 2) \
			* (cellView2.position - cellView1.position)

		cellView1.velocity = newVelocity1
		cellView2.velocity = newVelocity2

	def resolve(self, cellView1: CellView, cellView2: CellView) -> None:
		if not self.test(cellView1, cellView2):
			return
		self.collision(cellView1, cellView2)
