from BinarySearchTree import BinarySearchTree
from TreeNode import TreeNode

class AVLTree(BinarySearchTree):

	def __init__(self):
		super(AVLTree, self).__init__()

	# Returns the difference in heights of left and right subtrees of given node
	def get_balance(self, node):
		if node:
			return self.height(node.get_left()) - self.height(node.get_right())
		return 0

	# Rotates left on a given node
	def left_rotation(self, node):
		pivot = node.get_right()
		subtree = pivot.get_left()

		pivot.set_left(node)
		node.set_right(subtree)

		ht = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
		node.set_height(ht)
		ht = 1 + max(self.height(pivot.get_left()), self.height(pivot.get_right()))
		pivot.set_height(ht)

		return pivot

	# Rotates right on a given node
	def right_rotation(self, node):
		pivot = node.get_left()
		subtree = pivot.get_right()

		pivot.set_right(node)
		node.set_left(subtree)

		ht = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
		node.set_height(ht)
		ht = 1 + max(self.height(pivot.get_left()), self.height(pivot.get_right()))
		pivot.set_height(ht)

		return pivot

	# Inserts a node into the tree
	def insert(self, key):
		def insert(node, key):
			if not node:
				node = TreeNode(key)
			elif key < node.get_key():
				node.set_left(insert(node.get_left(), key))
			elif key > node.get_key():
				node.set_right(insert(node.get_right(), key))
			else:
				# Not adding if key already present
				pass			

			ht = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
			node.set_height(ht)
			balance = self.get_balance(node)
			
			
			if balance > 1:
				if key < node.get_left().get_key():
					node = self.right_rotation(node)
				else:
					node.set_left(self.left_rotation(node.get_left()))
					node = self.right_rotation(node)
		
			if balance < -1:
				if key > node.get_right().get_key():
					node = self.left_rotation(node)
				else:
					node.set_right(self.right_rotation(node.get_right()))
					node = self.left_rotation(node)

			return node

		self.set_root(insert(self.root, key))
		self.size = self.size + 1

	# Removes a node from the tree
	def remove(self, key):
		def remove(node, key):
			if not node:
				raise Exception('Key not found!')
			elif node.get_key() is key:
				if not node.has_left() and not node.has_right():
					node = None
				elif not node.has_left():
					node = node.get_right()
				elif not node.has_right():
					node = node.get_left()
				else:
					mini = self.minimum(node.get_right())
					node.set_key(mini.get_key())
					node.set_right(remove(node.get_right(), mini.get_key()))
			elif key < node.get_key():
				node.set_left(remove(node.get_left(), key))
			else:
				node.set_right(remove(node.get_right(), key))

			if node:
				ht = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
				node.set_height(ht)
				balance = self.get_balance(node)

				if balance > 1:
					if self.get_balance(node.get_left()) >= 0:
						node = self.right_rotation(node)
					if self.get_balance(node.get_left()) < 0:
						node.set_left(self.left_rotation(node.get_left()))
						node = self.right_rotation(node)

				if balance < -1:
					if self.get_balance(node.get_right()) <= 0:
						node = self.left_rotation(node)
					if self.get_balance(node.get_right()) > 0:
						node.set_right(self.right_rotation(node.get_right()))
						node = self.left_rotation(node)

			return node

		self.set_root(remove(self.root, key))
		self.size = self.size - 1