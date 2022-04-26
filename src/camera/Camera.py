from abc import ABC, abstractmethod
from src.engine.World import World


class Camera(ABC):
	@abstractmethod
	def display(self, world: World) -> None:
		pass
