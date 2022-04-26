from src.world.utils.atom.Atom import Atom
from src.world.physics.utils.joint.Joint import Joint
from src.world.physics.collisionresolver.CollisionResolver import CollisionResolver
from src.world.physics.jointresolver.JointResolver import JointResolver
from src.world.physics.utils.atomview.AtomView import AtomView
from src.world.physics.utils.jointview.JointView import JointView
from src.utils.dim2.Dim2 import Dim2
from src.world.physics.movementresolver.MovementResolver import MovementResolver
from src.world.utils.quadtree.Quadtree import Quadtree
from src.config.world.WorldConfig import WorldConfig
from src.utils.dim2.FloatDim2 import FloatDim2


class World:
	def __init__(
		self,
		*,
		collisionResolver: CollisionResolver,
		jointResolver: JointResolver,
		movementResolver: MovementResolver,
		config: WorldConfig,
		# size: Dim2,
	) -> None:
		self._atoms: set[Atom] = set[Atom]()
		self._joints: set[Joint] = set[Joint]()
		self.collisionResolver: CollisionResolver = collisionResolver
		self.jointResolver: JointResolver = jointResolver
		self.movementResolver: MovementResolver = movementResolver
		self._config: WorldConfig = config
		self._quadtree = Quadtree(
			minChunkSize=self._config.quadtree.chunks.minSize,
			maxChunkSize=self._config.quadtree.chunks.maxSize,
		)
		self._size: FloatDim2 = self._config.size

	@property
	def size(self) -> FloatDim2:
		return self._size

	def addAtom(self, atom: Atom) -> None:
		self._atoms.add(atom)
		self._quadtree.addAtom(atom)

	def addJoint(self, joint: Joint) -> None:
		self._joints.add(joint)

	@property
	def atoms(self) -> frozenset[Atom]:
		return frozenset(self._atoms)

	@property
	def joints(self) -> frozenset[Joint]:
		return frozenset(self._joints)

	@property
	def config(self) -> WorldConfig:
		return self._config

	def applyAtomView(self, atomView: AtomView) -> None:
		atom: Atom = atomView.atom
		self._quadtree.removeAtom(atom)
		atom.position = atomView.position
		atom.velocity = atomView.velocity
		self._quadtree.addAtom(atom)

	def applyJointView(self, jointView: JointView) -> None:
		atomView1: AtomView = jointView.atom1
		atomView2: AtomView = jointView.atom2
		self.applyAtomView(atomView1)
		self.applyAtomView(atomView2)

	def resolveCollisions(self, deltaTime: float) -> None:
		atomsList: list[Atom] = list(self.atoms)
		for i1 in range(len(atomsList)):
			atom1: Atom = atomsList[i1]
			possibleCollisions: set[Atom] = self._quadtree.getNeighbors(atom1)
			possibleCollisions.remove(atom1)
			for atom2 in possibleCollisions:
				atomView1: AtomView = AtomView(atom1)
				atomView2: AtomView = AtomView(atom2)
				self.collisionResolver.resolve(deltaTime, atomView1, atomView2)
				self.applyAtomView(atomView1)
				self.applyAtomView(atomView2)

	def resolveJoints(self, deltaTime: float) -> None:
		for joint in self.joints:
			jointView: JointView = JointView(joint)
			self.jointResolver.resolve(deltaTime, jointView)
			self.applyJointView(jointView)

	def resolveMovements(self, deltaTime: float) -> None:
		for atom in self.atoms:
			atomView: AtomView = AtomView(atom)
			self.movementResolver.resolve(deltaTime, atomView)
			self.applyAtomView(atomView)

	def tick(self, deltaTime: float) -> None:
		self.resolveCollisions(deltaTime)
		self.resolveMovements(deltaTime)
		self.resolveJoints(deltaTime)
