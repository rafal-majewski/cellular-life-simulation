from src.engine.Cell import Cell
from pygame.surface import Surface
from src.abstractcamera.AbstractMoveableCamera import AbstractMoveableCamera
import pygame
from src.engine.Point2 import Point2


class Drawer:
	def __init__(self, surface: Surface) -> None:
		self.surface = surface

	def drawCell(self, cell: Cell, camera: AbstractMoveableCamera) -> None:
		positionOnScreen: Point2 = cell.position - camera.position
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
