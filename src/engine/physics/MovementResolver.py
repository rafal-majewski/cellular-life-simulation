from src.engine.physics.CellView import CellView
from src.utils.point2.FloatPoint2 import FloatPoint2
import math


class MovementResolver:
	def resolve(self, cellView: CellView, deltaTime: float) -> None:
		# todo:
		# parameterize the class
		cellView.position += cellView.velocity * deltaTime
		cellView.velocity *= math.pow(0.95, deltaTime)
		# todo to remove:
		# temp:
		if cellView.position.x > 400.0:
			cellView.velocity = FloatPoint2(-abs(cellView.velocity.x), cellView.velocity.y)
		if cellView.position.x < -400:
			cellView.velocity = FloatPoint2(abs(cellView.velocity.x), cellView.velocity.y)
		if cellView.position.y > 300.0:
			cellView.velocity = FloatPoint2(cellView.velocity.x, -abs(cellView.velocity.y))
		if cellView.position.y < -300:
			cellView.velocity = FloatPoint2(cellView.velocity.x, abs(cellView.velocity.y))
