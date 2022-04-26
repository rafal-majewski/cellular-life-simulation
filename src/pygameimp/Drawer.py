from src.world.utils.atom.Atom import Atom
from pygame.surface import Surface
from src.camera.MoveableCamera import MoveableCamera
import pygame
from src.utils.point2.FloatPoint2 import FloatPoint2
# from src.world.quadtree.Chunk import Chunk
from src.utils.color.Color import Color

class Drawer:
	def __init__(self, surface: Surface) -> None:
		self.surface = surface

	def colorToTuple(self, color: Color) -> tuple[int, int, int]:
		return (color.r, color.g, color.b)

	@property
	def surfaceCenterPosition(self) -> FloatPoint2:
		return FloatPoint2(
			self.surface.get_width() / 2,
			self.surface.get_height() / 2,
		)

	def _translate(self, point: FloatPoint2, camera: MoveableCamera) -> FloatPoint2:
		return point \
			- camera.position \
			+ self.surfaceCenterPosition

	def drawAtom(self, atom: Atom, camera: MoveableCamera) -> None:
		positionOnScreen: FloatPoint2 = self._translate(atom.position, camera)
			
		pygame.draw.circle(
			self.surface,
			self.colorToTuple(atom.color),
			(int(positionOnScreen.x), int(positionOnScreen.y)),
			int(atom.radius)
		)

	def clear(self) -> None:
		self.surface.fill((255, 255, 255))

	def display(self) -> None:
		pygame.display.flip()

	# def drawChunk(self, chunk: Chunk, camera: AbstractMoveableCamera) -> None:
	# 	topLeft: FloatPoint2 = self._translate(
	# 		chunk.realPosition - FloatPoint2.fromDim2(chunk.size) / 2,
	# 		camera
	# 	)
	# 	pygame.draw.line(
	# 		self.surface,
	# 		(255, 0, 0),
	# 		(int(topLeft.x), int(topLeft.y)),
	# 		(int(topLeft.x + chunk.size.width), int(topLeft.y)),
	# 	)
	# 	pygame.draw.line(
	# 		self.surface,
	# 		(255, 0, 0),
	# 		(int(topLeft.x), int(topLeft.y)),
	# 		(int(topLeft.x), int(topLeft.y + chunk.size.height)),
	# 	)
	# 	pygame.draw.line(
	# 		self.surface,
	# 		(255, 0, 0),
	# 		(int(topLeft.x + chunk.size.width), int(topLeft.y)),
	# 		(int(topLeft.x + chunk.size.width), int(topLeft.y + chunk.size.height)),
	# 	)
	# 	pygame.draw.line(
	# 		self.surface,
	# 		(255, 0, 0),
	# 		(int(topLeft.x), int(topLeft.y + chunk.size.height)),
	# 		(int(topLeft.x + chunk.size.width), int(topLeft.y + chunk.size.height)),
	# 	)

