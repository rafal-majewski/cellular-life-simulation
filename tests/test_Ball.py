from unittest import TestCase
from src.Ball import Ball
from src.Point2 import Point2


class Test_Ball(TestCase):
	def test_constructor(self):
		velocity: Point2 = Point2(1, 2)
		position: Point2 = Point2(3, 4)
		mass: float = 5.0
		radius: float = 10.0
		ball: Ball = Ball(
			position=position,
			velocity=velocity,
			mass=mass,
			radius=radius
		)
		self.assertEqual(ball.position, position)
		self.assertEqual(ball.velocity, velocity)
		self.assertEqual(ball.mass, mass)
		self.assertEqual(ball.radius, radius)

	def test_mass_setter(self):
		ball: Ball = Ball(
			position=Point2(1, 2),
			velocity=Point2(3, 4),
			mass=5.0,
			radius=10.0
		)
		newMass: float = 10.0
		ball.mass = newMass
		self.assertEqual(ball.mass, newMass)

	def test_radius_setter(self):
		ball: Ball = Ball(
			position=Point2(1, 2),
			velocity=Point2(3, 4),
			mass=5.0,
			radius=10.0
		)
		newRadius: float = 10.0
		ball.radius = newRadius
		self.assertEqual(ball.radius, newRadius)
