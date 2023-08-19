class TreeNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

	# height/depth
	def height(self):
		if self is None:
			return 0
		return 1+max(TreeNode.height(self.left),TreeNode.height(self.right))

	def size(self):
		if self is None:
			return 0
		return 1+TreeNode.size(self.left)+TreeNode.size(self.right)

	@staticmethod
	def parse_tuple(data):
		if data is None:
			node = None
		if isinstance(data,tuple) and len(data)==3:
			node = TreeNode(data[1])
			node.left = TreeNode.parse_tuple(data[0])
			node.right = TreeNode.parse_tuple(data[2])
		else:
			node = TreeNode(data)
		return node

	def to_tuple(self):
		if self is None:
			return None
		else:
			return ((TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)))

	def display(self, space='\t', level=0):
		if self is None:
			print(space*level + ' ')
			return

		if self.left is None and self.right is None:
			print(space*level + str(self.key))
			return

		TreeNode.display(self.right, space, level+1)
		print(space*level + str(self.key))
		TreeNode.display(self.left,space, level+1)

	def traverse(self,order):
		if self is None:
			return []
		if(order=='in'):
			return(TreeNode.traverse(self.left,order) + [self.key] + TreeNode.traverse(self.right,order))
		if(order=='pre'):
			return([self.key] + TreeNode.traverse(self.left,order) + TreeNode.traverse(self.right,order))
		if(order=='post'):
			return(TreeNode.traverse(self.left,order) + TreeNode.traverse(self.right,order) + [self.key])

	@staticmethod
	def remove_none(lst):
		return [key for key in lst if key is not None]

	# returns is_bst, min key and max key (binary search tree)
	def is_bst(self):
		if self is None:
			return True, None, None

		is_bst_left, min_left, max_left = self.left.is_bst() if self.left else (True, None, None)
		is_bst_right, min_right, max_right = self.right.is_bst() if self.right else (True, None, None)
		is_bst_node = is_bst_left and is_bst_right and (max_left is None or self.key > max_left) and (min_right is None or self.key < min_right)

		none_removed = TreeNode.remove_none([min_left, self.key, min_right])
		min_key = min(none_removed) if none_removed else None
		none_removed = TreeNode.remove_none([max_left, self.key, max_right])
		max_key = max(none_removed) if none_removed else None

		return is_bst_node, min_key, max_key

tree = TreeNode.parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))
# tree = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
# tree = TreeNode.parse_tuple((((7,11,2),4,None),5,(13,8,(None,4,1))))
# BST
# tree = TreeNode.parse_tuple(((-1, 1, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print("Tree data :",tree.to_tuple())
print("\nTree depth/height :",tree.height())
print("\nTree size :",tree.size())
print("\nIn order traversal :",tree.traverse('in'))
print("\nPre order traversal :",tree.traverse('pre'))
print("\nPost order traversal :",tree.traverse('post'))
print("\nIs BST, Min Key, Max Key",tree.is_bst())
print("\nTree display :\n")
print(tree.display())