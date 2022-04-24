from src.abstractcamera.AbstractMoveableCamera import AbstractMoveableCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer
from src.utils.Point2 import Point2


class Camera(AbstractMoveableCamera):
	def __init__(self, *, drawer: Drawer, position: Point2) -> None:
		super().__init__(position=position)
		self.drawer = drawer

	def display(self, world: World) -> None:
		self.drawer.clear()
		for cell in world.cells:
			self.drawer.drawCell(cell, self)
		self.drawer.display()
