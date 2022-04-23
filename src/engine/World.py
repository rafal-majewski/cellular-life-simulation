from src.engine.Cell import Cell
from src.utils.Point2 import Point2
from src.engine.Joint import Joint


class World:
	def __init__(self) -> None:
		self.cells = set[Cell]()
		self.joints = set[Joint]()

	def addCell(self, cell: Cell) -> None:
		self.cells.add(cell)

	def addJoint(self, joint: Joint) -> None:
		self.joints.add(joint)

	def testCellCellCollision(self, cell1: Cell, cell2: Cell) -> bool:
		return \
			(cell1.position - cell2.position).magnitude \
			< cell1.radius + cell2.radius

	def cellCellCollision(self, cell1: Cell, cell2: Cell) -> None:
		# print("cellCellCollision")
		# https://en.wikipedia.org/wiki/Elastic_collision
		
		
		# check if the cells should bounce
		if (cell1.velocity - cell2.velocity).dotProduct(cell1.position - cell2.position) >= 0:
			return

		distance: float = (cell1.position - cell2.position).magnitude

		newVelocity1: Point2 = \
			cell1.velocity \
			- 2 * cell2.mass / (cell1.mass + cell2.mass) \
			* ((cell1.velocity - cell2.velocity).dotProduct(cell1.position - cell2.position)) \
			/ (distance ** 2) \
			* (cell1.position - cell2.position)
		newVelocity2: Point2 = \
			cell2.velocity \
			- 2 * cell1.mass / (cell1.mass + cell2.mass) \
			* ((cell2.velocity - cell1.velocity).dotProduct(cell2.position - cell1.position)) \
			/ (distance ** 2) \
			* (cell2.position - cell1.position)

		cell1.velocity = newVelocity1
		cell2.velocity = newVelocity2

	def resolveCellCellCollision(self, cell1: Cell, cell2: Cell) -> None:
		if not self.testCellCellCollision(cell1, cell2):
			return
		self.cellCellCollision(cell1, cell2)

	def resolveCollisions(self) -> None:
		for cell1 in self.cells:
			for cell2 in self.cells:
				if cell1 == cell2:
					continue
				self.resolveCellCellCollision(cell1, cell2)

	def resolveJoint(self, joint: Joint) -> None:
		jointDistance: float = joint.cell1.radius + joint.cell2.radius
		
		dir1: Point2 = (joint.cell2.position - joint.cell1.position).normalize()
		dir2: Point2 = (joint.cell1.position - joint.cell2.position).normalize()
		missingDist: float = (joint.cell2.position - joint.cell1.position).magnitude - jointDistance
		mag1: float = missingDist * joint.cell1.mass / (joint.cell1.mass + joint.cell2.mass)
		mag2: float = missingDist * joint.cell2.mass / (joint.cell1.mass + joint.cell2.mass)
		joint.cell1.velocity += mag1 * dir1 * joint.stiffness
		joint.cell2.velocity += mag2 * dir2 * joint.stiffness

	def resolveJoints(self) -> None:
		for joint in self.joints:
			self.resolveJoint(joint)

	def tick(self, deltaTime: float) -> None:
		self.resolveCollisions()
		for cell in self.cells:
			cell.position += cell.velocity * deltaTime
		self.resolveJoints()
		energy: float = 0
		for cell in self.cells:
			energy += cell.mass * cell.velocity.magnitude ** 2 / 2
		print("energia układu:", energy)
