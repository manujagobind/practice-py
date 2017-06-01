class TreeNode(object):
	
	def __init__(self, key):
		self.key = key
		self.height = 0
		self.left, self.right  = None, None

	def get_key(self):
		return self.key

	def set_key(self, key):
		self.key = key

	def get_height(self):
		return self.height

	def set_height(self, height):
		self.height = height

	# Returns true if node has a left child
	def has_left(self):
		return self.left is not None

	def get_left(self):
		return self.left

	def set_left(self, left):
		self.left = left

	# Returns true if node has a right child
	def has_right(self):
		return self.right is not None

	def get_right(self):
		return self.right

	def set_right(self, right):
		self.right = right
