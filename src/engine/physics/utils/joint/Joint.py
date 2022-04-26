from src.engine.utils.atom.Atom import Atom


class Joint:
	def __init__(
		self,
		*,
		atom1: Atom,
		atom2: Atom,
		stiffness: float,
	) -> None:
		self.atom1: Atom = atom1
		self.atom2: Atom = atom2
		self.stiffness: float = stiffness

	@property
	def restDistance(self) -> float:
		return self.atom1.radius + self.atom2.radius

	def __str__(self) -> str:
		return (
			f"Joint("
			f"atom1={self.atom1}, "
			f"atom2={self.atom2}, "
			f"stiffness={self.stiffness}"
			f")"
		)
