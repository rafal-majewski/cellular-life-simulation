from src.engine.Cell import Cell
from pygame.surface import Surface
import pygame


class Drawer:
	def __init__(self, surface: Surface) -> None:
		self.surface = surface

	def drawCell(self, cell: Cell) -> None:
		pass

	def clear(self) -> None:
		self.surface.fill((255, 255, 255))

	def display(self) -> None:
		pygame.display.flip()
