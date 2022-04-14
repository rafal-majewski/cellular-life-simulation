from unittest import TestCase
from src.engine.Entity import Entity
from src.utils.Point2 import Point2


class Test_Entity(TestCase):
	def test_constructor(self):
		velocity: Point2 = Point2(1, 2)
		position: Point2 = Point2(3, 4)
		entity: Entity = Entity(position=position, velocity=velocity)
		self.assertEqual(entity.position, position)
		self.assertEqual(entity.velocity, velocity)

	def test_position_setter(self):
		entity: Entity = Entity(position=Point2(1, 2), velocity=Point2(3, 4))
		newPosition: Point2 = Point2(5, 6)
		entity.position = newPosition
		self.assertEqual(entity.position, newPosition)

	def test_velocity_setter(self):
		entity: Entity = Entity(position=Point2(1, 2), velocity=Point2(3, 4))
		newVelocity: Point2 = Point2(5, 6)
		entity.velocity = newVelocity
		self.assertEqual(entity.velocity, newVelocity)
