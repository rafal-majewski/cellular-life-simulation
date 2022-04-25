from src.abstractcamera.AbstractMoveableCamera import AbstractMoveableCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer
from src.utils.point2.FloatPoint2 import FloatPoint2


class Camera(AbstractMoveableCamera):
	def __init__(self, *, drawer: Drawer, position: FloatPoint2) -> None:
		super().__init__(position=position)
		self.drawer = drawer

	def display(self, world: World) -> None:
		self.drawer.clear()
		for cell in world.cells:
			self.drawer.drawCell(cell, self)
		self.drawer.display()
