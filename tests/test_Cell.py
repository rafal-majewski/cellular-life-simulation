from unittest import TestCase
from src.Cell import Cell
from src.Point2 import Point2


class Test_Cell(TestCase):
	def test_constructor(self):
		velocity: Point2 = Point2(1, 2)
		position: Point2 = Point2(3, 4)
		mass: float = 5.0
		radius: float = 10.0
		cell: Cell = Cell(
			position=position,
			velocity=velocity,
			mass=mass,
			radius=radius
		)
		self.assertEqual(cell.position, position)
		self.assertEqual(cell.velocity, velocity)
		self.assertEqual(cell.mass, mass)
		self.assertEqual(cell.radius, radius)

	def test_mass_setter(self):
		cell: Cell = Cell(
			position=Point2(1, 2),
			velocity=Point2(3, 4),
			mass=5.0,
			radius=10.0
		)
		newMass: float = 10.0
		cell.mass = newMass
		self.assertEqual(cell.mass, newMass)

	def test_radius_setter(self):
		cell: Cell = Cell(
			position=Point2(1, 2),
			velocity=Point2(3, 4),
			mass=5.0,
			radius=10.0
		)
		newRadius: float = 10.0
		cell.radius = newRadius
		self.assertEqual(cell.radius, newRadius)
