from unittest import TestCase
from src.Point2 import Point2


class Test_Point2(TestCase):
	def test_constructor(self):
		p: Point2 = Point2(1, 2)
		self.assertEqual(p.x, 1)
		self.assertEqual(p.y, 2)

	def test_x_immutability(self):
		p: Point2 = Point2(1, 2)
		with self.assertRaises(AttributeError):
			p.x = 3

	def test_y_immutability(self):
		p: Point2 = Point2(1, 2)
		with self.assertRaises(AttributeError):
			p.y = 3

	def test_str(self):
		p: Point2 = Point2(1, 2)
		self.assertEqual(str(p), "Point2(1, 2)")

	def test_repr(self):
		p: Point2 = Point2(1, 2)
		self.assertEqual(repr(p), "Point2(1, 2)")

	def test_eq_with_same_point(self):
		p: Point2 = Point2(1, 2)
		self.assertTrue(p == p)

	def test_eq_with_different_point(self):
		p1: Point2 = Point2(1, 2)
		p2: Point2 = Point2(2, 3)
		self.assertFalse(p1 == p2)

	def test_eq_with_different_type(self):
		p: Point2 = Point2(1, 2)
		self.assertFalse(p == 1)

	def test_eq_with_pair(self):
		p: Point2 = Point2(1, 2)
		self.assertFalse(p == (1, 2))

	def test_eq_with_equal_point(self):
		p1: Point2 = Point2(1, 2)
		p2: Point2 = Point2(1, 2)
		self.assertTrue(p1 == p2)

	def test_add(self):
		p1: Point2 = Point2(1, 2)
		p2: Point2 = Point2(2, 3)
		self.assertEqual(p1 + p2, Point2(3, 5))

	def test_sub(self):
		p1: Point2 = Point2(1, 2)
		p2: Point2 = Point2(2, 3)
		self.assertEqual(p1 - p2, Point2(-1, -1))

	def test_mul_by_scalar(self):
		p: Point2 = Point2(1, 2)
		self.assertEqual(p * 2, Point2(2, 4))

	def test_div_by_scalar(self):
		p: Point2 = Point2(2, 4)
		self.assertEqual(p / 2, Point2(1, 2))
