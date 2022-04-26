from src.engine.utils.atom.Atom import Atom


class Air(Atom):
	def __str__(self) -> str:
		return (
			f"Air("
			f"position={self.position}, "
			f"velocity={self.velocity}"
			f")"
		)
