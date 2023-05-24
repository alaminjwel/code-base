class TreeNode:
	def __init__(self,key,left=None,right=None):
		self.key = key
		self.left = left
		self.right = right

	def height(self):
		if self is None:
			return 0
		return 1+max(TreeNode.height(self.left),TreeNode.height(self.right))

	def size(self):
		if self is None:
			return 0
		return 1+TreeNode.size(self.left)+TreeNode.size(self.right)

	def traverse(self,order):
		if self is None:
			return []
		left,right,node = self.left,self.right,self.key
		if order=='pre':
			return [[node]+TreeNode.traverse(left,order)+TreeNode.traverse(right,order)]
		elif order=='in':
			return [TreeNode.traverse(left,order),[node]+TreeNode.traverse(right,order)]
		else:
			return [TreeNode.traverse(left,order)+TreeNode.traverse(right,order),[node]]


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

	def to_tupple(self):
		if self is None:
			return None
		return ((TreeNode.to_tupple(self.left),self.key,TreeNode.to_tupple(self.right)))

	def display(self,space='\t',level=0):
		if self is None:
			print(space*level,' ')
			return

		if self.left is None and self.right is None:
			print(space*level,str(self.key))
			return
		TreeNode.display(self.left,space,level+1)
		print(space*level,str(self.key))
		TreeNode.display(self.right,space,level+1)

tree = TreeNode.parse_tuple(((1,3,None),2,((None,3,4),5,(6,7,8))))
tree.display()
print("\nTree depth/height :",tree.height())
print("\nTree size :",tree.size())
print("Tree data :",tree.to_tupple())
# print("\nIn order traversal :",tree.traverse('in'))
print("\nPre order traversal :",tree.traverse('pre'))
# print("\nPost order traversal :",tree.traverse('post'))