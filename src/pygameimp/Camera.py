from src.abstractcamera.AbstractCamera import AbstractCamera
from src.engine.World import World
from src.pygameimp.Drawer import Drawer


class Camera(AbstractCamera):
	def __init__(self, drawer: Drawer) -> None:
		self.drawer = drawer

	def display(self, world: World) -> None:
		for cell in world.cells:
			self.drawer.drawCell(cell)
