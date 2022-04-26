from src.camera.MoveableCamera import MoveableCamera
from src.engine.world.World import World
from src.pygameimp.Drawer import Drawer
from src.utils.point2.FloatPoint2 import FloatPoint2
from src.engine.utils.quadtree.Quadtree import Quadtree


class PygameCamera(MoveableCamera):
	def __init__(self, *, drawer: Drawer, position: FloatPoint2) -> None:
		super().__init__(position=position)
		self.drawer = drawer

	def display(self, world: World) -> None:
		self.drawer.clear()
		for atom in world.atoms:
			self.drawer.drawAtom(atom, self)
		# quadtree: Quadtree = world.quadtree
		# for y in quadtree._mainChunks:
		# 	for x in quadtree._mainChunks[y]:
		# 		self.drawer.drawChunk(quadtree._mainChunks[y][x], self)
		self.drawer.display()
