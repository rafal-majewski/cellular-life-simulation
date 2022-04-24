from abc import ABC, abstractmethod


class Gene(ABC):
	@abstractmethod
	def mutate(self, rate: float) -> None:
		pass
