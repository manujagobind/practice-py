from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree

def summary(tree):
	print 'Max:\t', tree.maximum(tree.get_root()).get_key()	
	print 'Min:\t', tree.minimum(tree.get_root()).get_key()		
	print 'Height:\t', tree.get_height()
	print 'Size:\t', tree.get_size()		
	print 'Is BST?\t', tree.is_bst()
	print '\n'

def main():
	trees = [BinarySearchTree(), AVLTree()]

	for tree in trees:
		tree.insert(5)
		tree.insert(9)
		tree.insert(2)
		tree.insert(8)
		tree.insert(1)
		tree.insert(7)
		tree.insert(6)
		tree.insert(3)
		tree.insert(4)

	for tree in trees:
		print tree
		print 'Inorder:'
		tree.inorder()
		print 'Levelorder:'
		tree.levelorder()
		print 'Level by Level'
		tree.level_by_level()		
		summary(tree)

if __name__ == '__main__':
	main()