from src.engine.Cell import Cell
from pygame.surface import Surface
from src.abstractcamera.AbstractMoveableCamera import AbstractMoveableCamera
import pygame
from src.utils.point2.FloatPoint2 import FloatPoint2


class Drawer:
	def __init__(self, surface: Surface) -> None:
		self.surface = surface

	@property
	def surfaceCenterPosition(self) -> FloatPoint2:
		return FloatPoint2(self.surface.get_width() / 2, self.surface.get_height() / 2)

	def drawCell(self, cell: Cell, camera: AbstractMoveableCamera) -> None:
		positionOnScreen: FloatPoint2 = cell.position \
			- camera.position \
			+ self.surfaceCenterPosition
		pygame.draw.circle(
			self.surface,
			(0, 0, 0),
			(int(positionOnScreen.x), int(positionOnScreen.y)),
			int(cell.radius)
		)

	def clear(self) -> None:
		self.surface.fill((255, 255, 255))

	def display(self) -> None:
		pygame.display.flip()
