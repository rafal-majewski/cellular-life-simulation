# Wrapper class for preventing direct modification of
# atom's position and velocity

from src.world.utils.atom.Atom import Atom
from src.world.physics.utils.entityview.EntityView import EntityView


class AtomView(EntityView):
	def __init__(self, atom: Atom) -> None:
		super().__init__(atom)
		self._atom: Atom = atom

	@property
	def atom(self) -> Atom:
		return self._atom

	@property
	def mass(self) -> float:
		return self._atom.mass

	@property
	def radius(self) -> float:
		return self._atom.radius

	def __str__(self) -> str:
		return (
			f"AtomView("
			f"atom={self._atom}, "
			f"position={self.position}, "
			f"velocity={self.velocity}"
			f")"
		)
