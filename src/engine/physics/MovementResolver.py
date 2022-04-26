from src.engine.physics.utils.atomview.AtomView import AtomView
import math


class MovementResolver:
	def resolve(self, deltaTime: float, atomView: AtomView) -> None:
		atomView.position += atomView.velocity * deltaTime
		atomView.velocity *= math.pow(0.95, deltaTime)
