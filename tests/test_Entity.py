from unittest import TestCase
from src.Entity import Entity
from src.Point2 import Point2


class Test_Entity(TestCase):
	def test_constructor(self):
		velocity: Point2 = Point2(1, 2)
		position: Point2 = Point2(3, 4)
		entity: Entity = Entity(position=position, velocity=velocity)
		self.assertEqual(entity.position, position)
		self.assertEqual(entity.velocity, velocity)
