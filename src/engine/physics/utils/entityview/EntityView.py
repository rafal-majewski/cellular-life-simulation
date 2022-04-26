# Wrapper class for preventing direct modification of
# atom's position and velocity

from src.engine.utils.boundingbox2.BoundingBox2 import BoundingBox2
from src.engine.utils.entity.Entity import Entity


class EntityView(Entity):
	def __init__(self, entity: Entity) -> None:
		super().__init__(
			position=entity.position,
			velocity=entity.velocity,
		)
		self._entity: Entity = entity

	@property
	def entity(self) -> Entity:
		return self._entity

	@property
	def boundingBox(self) -> BoundingBox2:
		return self._entity.boundingBox

	def __str__(self) -> str:
		return (
			f"EntityView("
			f"entity={self._entity}, "
			f"position={self.position}, "
			f"velocity={self.velocity}"
			f")"
		)
