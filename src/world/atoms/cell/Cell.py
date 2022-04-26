from src.world.utils.atom.Atom import Atom


class Cell(Atom):
	def __str__(self) -> str:
		return (
			f"Cell("
			f"position={self.position}, "
			f"velocity={self.velocity}"
			f")"
		)
