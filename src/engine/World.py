from src.engine.Cell import Cell
from src.engine.Joint import Joint
from src.engine.physics.CollisionResolver import CollisionResolver
from src.engine.physics.JointResolver import JointResolver
from src.engine.physics.CellView import CellView
from src.engine.physics.JointView import JointView
from src.engine.physics.MovementResolver import MovementResolver


class World:
	def __init__(
		self,
		*,
		collisionResolver: CollisionResolver,
		jointResolver: JointResolver,
		movementResolver: MovementResolver,
	) -> None:
		self._cells: set[Cell] = set[Cell]()
		self._joints: set[Joint] = set[Joint]()
		self.collisionResolver: CollisionResolver = collisionResolver
		self.jointResolver: JointResolver = jointResolver
		self.moveResolver: MovementResolver = movementResolver

	def addCell(self, cell: Cell) -> None:
		self._cells.add(cell)

	def addJoint(self, joint: Joint) -> None:
		self._joints.add(joint)

	@property
	def cells(self) -> frozenset[Cell]:
		return frozenset(self._cells)

	@property
	def joints(self) -> frozenset[Joint]:
		return frozenset(self._joints)

	def applyCellView(self, cellView: CellView) -> None:
		cell: Cell = cellView._cell
		cell.position = cellView.position
		cell.velocity = cellView.velocity

	def applyJointView(self, jointView: JointView) -> None:
		cellView1: CellView = jointView.cell1
		cellView2: CellView = jointView.cell2
		self.applyCellView(cellView1)
		self.applyCellView(cellView2)

	def resolveCollisions(self, deltaTime: float) -> None:
		cellsList: list[Cell] = list(self.cells)
		for i1 in range(len(cellsList)):
			cell1: Cell = cellsList[i1]
			for i2 in range(i1 + 1, len(cellsList)):
				cell2: Cell = cellsList[i2]
				cellView1: CellView = CellView(cell1)
				cellView2: CellView = CellView(cell2)
				self.collisionResolver.resolve(cellView1, cellView2)
				self.applyCellView(cellView1)
				self.applyCellView(cellView2)

	def resolveJoints(self, deltaTime: float) -> None:
		for joint in self.joints:
			jointView: JointView = JointView(joint)
			self.jointResolver.resolve(jointView)
			self.applyJointView(jointView)

	def resolveMovements(self, deltaTime: float) -> None:
		for cell in self.cells:
			cellView: CellView = CellView(cell)
			self.moveResolver.resolve(cellView, deltaTime)
			self.applyCellView(cellView)

	def tick(self, deltaTime: float) -> None:
		self.resolveCollisions(deltaTime)
		self.resolveMovements(deltaTime)
		self.resolveJoints(deltaTime)
