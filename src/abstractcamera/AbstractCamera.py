from abc import ABC, abstractmethod
from src.engine import World


class AbstractCamera(ABC):
	@abstractmethod
	def display(self, world: World) -> None:
		pass
