from unittest import TestCase
from src.world.utils.atom.Atom import Atom
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.utils.color.Color import Color


class Test_Atom(TestCase):
	def test_constructor(self):
		velocity: FloatPoint2 = FloatPoint2(1, 2)
		position: FloatPoint2 = FloatPoint2(3, 4)
		mass: float = 5.0
		radius: float = 10.0
		atom: Atom = Atom(
			position=position,
			velocity=velocity,
			mass=mass,
			radius=radius,
			color=Color(1, 1, 1),
		)
		self.assertEqual(atom.position, position)
		self.assertEqual(atom.velocity, velocity)
		self.assertEqual(atom.mass, mass)
		self.assertEqual(atom.radius, radius)

	def test_mass_setter(self):
		atom: Atom = Atom(
			position=FloatPoint2(1, 2),
			velocity=FloatPoint2(3, 4),
			mass=5.0,
			radius=10.0,
			color=Color(1, 1, 1),
		)
		newMass: float = 10.0
		atom.mass = newMass
		self.assertEqual(atom.mass, newMass)

	def test_radius_setter(self):
		atom: Atom = Atom(
			position=FloatPoint2(1, 2),
			velocity=FloatPoint2(3, 4),
			mass=5.0,
			radius=10.0,
			color=Color(1, 1, 1),
		)
		newRadius: float = 10.0
		atom.radius = newRadius
		self.assertEqual(atom.radius, newRadius)
