from src.engine.physics.CellView import CellView
import math


class MovementResolver:
	def resolve(self, cellView: CellView, deltaTime: float) -> None:
		cellView.position += cellView.velocity * deltaTime
		cellView.velocity *= math.pow(0.95, deltaTime)
