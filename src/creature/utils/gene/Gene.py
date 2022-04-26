from abc import ABC, abstractmethod


class Gene(ABC):
	def __init__(self, id: str) -> None:
		self._id: str = id

	@abstractmethod
	def mutate(self, rate: float) -> None:
		pass
