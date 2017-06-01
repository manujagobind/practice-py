from TreeNode import TreeNode

class BinarySearchTree(object):
	
	def __init__(self):
		self.root = None		
		self.size = 0

	# Getter
	def get_root(self):
		return self.root

	# Setter
	def set_root(self, root):
		self.root = root

	# Inorder traversal
	def inorder(self):
		def inorder(node):
			if node:
				inorder(node.get_left())
				print node.get_key(), " ",
				inorder(node.get_right())
		inorder(self.root)		
		print

	# Preorder traversal
	def preorder(self):
		def preorder(node):
			if node:
				print node.get_key(), " ",
				preorder(node.get_left())
				preorder(node.get_right())
		preorder(self.root)		
		print

	# Postorder traversal
	def postorder(self):
		def postorder(node):
			if node:
				postorder(node.get_left())
				postorder(node.get_right())
				print node.get_key(), " ",			
		postorder(self.root)	
		print

	# Levelorder traversal
	def levelorder(self):
		queue = list()
		
		queue.append(self.root)
		while queue:
			node = queue.pop(0)
			print node.get_key(), " ",
			if node.has_left():
				queue.append(node.get_left())
			if node.has_right():
				queue.append(node.get_right())
		print

	# Print all nodes at a given level
	def print_level(self, node, level):
		if node:
			if level == 0:
				print node.get_key(), " ",
			else:
				self.print_level(node.get_left(), level-1)
				self.print_level(node.get_right(), level-1)

	# Print nodes level by level
	def level_by_level(self):
		h = self.height(self.root) + 1
		for i in range(h):
			self.print_level(self.root, i)
			print

	# Returns height of the subtree
	def height(self, node):
		if node:
			return node.get_height()
		return -1;

	# Returns height of the tree
	def get_height(self):
		return self.height(self.root)

	# Returns number of nodes the tree
	def get_size(self):
		return self.size

	# Get node with minimum key
	def minimum(self, node):			
		if node:
			while node.has_left():
				node = node.get_left()
		return node

	# Get node with maximum key
	def maximum(self, node):
		if node:			
			while node.has_right():
				node = node.get_right()
		return node

	# Insert a node into the tree
	def insert(self, key):
		def insert(node, key):
			if not node:
				node = TreeNode(key)
			elif key < node.get_key():
				node.set_left(insert(node.get_left(), key))
			elif key > node.get_key():
				node.set_right(insert(node.get_right(), key))
			else:
				pass

			ht = 1 + max(self.height(node.get_left()), self.height(node.get_right()))
			node.set_height(ht)		
			return node

		self.set_root(insert(self.root, key))		
		self.size = self.size + 1	

	# Remove a node from the tree
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
			return node

		self.set_root(remove(self.root, key))		
		self.size = self.size - 1	

	# Returns true if given key exists in the tree
	def search(self, key):
		def search(node, key):
			if node:
				if node.get_key() is key:
					return True
				elif key < node.get_key():
					return search(node.get_left(), key)
				else:
					return search(node.get_right(), key)
			else:
				return False
		return search(self.root, key)

	# Returns node with given key
	def get_node(self, key):
		def get_node(node, key):
			if node:
				if node.get_key() is key:
					return node
				elif key < node.get_key():
					return get_node(node.get_left(), key)
				else:
					return get_node(node.get_right(), key)
			else:
				# Returns None if node with given key doesn't exist
				return None
		return get_node(self.root, key)

	# Returns node with next higher key in the tree
	def successor(self, key):
		node = self.get_node(key)
		if node:
			if node.has_right():
				return self.minimum(node.get_right())
			else:
				succ = None
				node = self.root
				while node:
					if key < node.get_key():
						succ = node
						node = node.get_left()
					elif key > node.get_key():
						node = node.get_right()
					else:
						break				
				# Returns None if successor doesn't exist
				return succ				
		else:
			raise Exception('Key not found!')

	def predecessor(self, key):
		node = self.get_node(key)
		if node:
			if node.has_left():
				return self.maximum(node.get_left())
			else:
				pred = None
				node = self.root
				while node:
					if key < node.get_key():
						node = node.get_left()
					elif key > node.get_key():
						pred = node
						node = node.get_right()
					else:
						break				
				# Returns None if predecessor doesn't exist
				return None				
		else:
			raise Exception('Key not found!')

	def is_bst(self):	
		def is_bst(node, mini, maxi):
			if node is None:
				return True
			elif node.get_key() < mini or node.get_key() > maxi:
				return False					
			else:
				return is_bst(node.get_left(), mini, node.get_key()) and is_bst(node.get_right(), node.get_key(), maxi)
		return is_bst(self.root, self.minimum(self.root).get_key(), self.maximum(self.root).get_key())
