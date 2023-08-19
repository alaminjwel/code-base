class BSTNode:
	def __init__(self, key, value=None):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	# height/depth
	def height(self):
		if self is None:
			return 0
		return 1+max(BSTNode.height(self.left),BSTNode.height(self.right))

	def size(self):
		if self is None:
			return 0
		return 1+BSTNode.size(self.left)+BSTNode.size(self.right)

	def to_tuple(self):
		if self is None:
			return None
		else:
			return ((BSTNode.to_tuple(self.left), self.key, BSTNode.to_tuple(self.right)))

	def display(self, space='\t', level=0):
		if self is None:
			print(space*level + ' ')
			return

		if self.left is None and self.right is None:
			print(space*level + str(self.key))
			return

		BSTNode.display(self.right, space, level+1)
		print(space*level + str(self.key))
		BSTNode.display(self.left,space, level+1)

	def traverse(self,order):
		if self is None:
			return []
		if(order=='in'):
			return(BSTNode.traverse(self.left,order) + [self.key] + BSTNode.traverse(self.right,order))
		if(order=='pre'):
			return([self.key] + BSTNode.traverse(self.left,order) + BSTNode.traverse(self.right,order))
		if(order=='post'):
			return(BSTNode.traverse(self.left,order) + BSTNode.traverse(self.right,order) + [self.key])

	def insert(self,key,value):
		if self is None:
			return BSTNode(key,value)
		if key<self.key:
			self.left = BSTNode.insert(self.left,key,value)
			self.left.parent = self
		elif key>self.key:
			self.right = BSTNode.insert(self.right,key,value)
			self.right.parent = self
		return self

	def find(self,key):
		if self is None:
			return None
		if self.key == key:
			return self
		if key<self.key:
			return BSTNode.find(self.left,key)
		if key>self.key:
			return BSTNode.find(self.right,key)

	def update(self,key,value):
		found = self.find(key)
		if found is not None:
			found.value = value

	def list_all(self):
		if self is None:
			return []
		return BSTNode.list_all(self.left) + [(self.key,self.value)] + BSTNode.list_all(self.right)

	# returns is_balanced (bool), height
	def is_balanced(self):
		if not self:
			return True,0
		is_balanced_left,height_left = BSTNode.is_balanced(self.left)
		is_balanced_right,height_right = BSTNode.is_balanced(self.right)
		is_balanced = is_balanced_left and is_balanced_right and abs(height_left-height_right)<=1
		height = 1+max(height_left,height_right)
		return is_balanced,height

	# make a balanced bst from a key,value list
	@classmethod
	def make_balanced_bst(cls,data,lo=0,hi=None,parent=None):
		if hi is None:
			hi = len(data)-1
		if lo>hi:
			return None
		mid = (lo+hi)//2
		key,value = data[mid]

		root = cls(key,value)
		root.parent=parent
		root.left = cls.make_balanced_bst(data,lo,mid-1,root)
		root.right = cls.make_balanced_bst(data,mid+1,hi,root)
		return root

	# convert unbalanced key to balanced
	def to_balanced(self):
		return BSTNode.make_balanced_bst(self.list_all())


# Balanced BST
# tree = BSTNode('jadesh','jadesh.username')
# tree.insert('biraj','biraj.username')
# tree.insert('sonaksh','sonaksh.username')
# tree.insert('aakash','aakash.username')
# tree.insert('hemanth','hemanth.username')
# tree.insert('sidhant','sidhant.username')
# tree.insert('vishal','vishal.username')

# Make banlaced tree using key value paired list
# pair_list = [("aakash", "aakash.username"),("biraj", "biraj.username"),("hemanth", "hemanth.username"),("jadesh", "jadesh.username"), ("sidhant", "sidhant.username"),("sonaksh", "sonaksh.username"),("vishal", "vishal.username")]
# tree = BSTNode.make_balanced_bst(pair_list)


# Unbalanced BST
tree = BSTNode('aakash','aakash.username')
tree.insert('biraj','biraj.username')
tree.insert('hemanth','hemanth.username')
tree.insert('jadesh','jadesh.username')
tree.insert('sidhant','sidhant.username')
tree.insert('sonaksh','sonaksh.username')
tree.insert('vishal','vishal.username')
tree.update('hemanth','hemanth.username-updated')
tree = tree.to_balanced()

print("\nTree depth/height :",tree.height())
print("\nTree size :",tree.size())

is_balanced,height = tree.is_balanced()
print("\nIs balanced : ",is_balanced)

find = 'hemanth'
found = tree.find(find)
if found is None:
	print("\nFind '"+find+"' : Not found")
else:
	print("\nFind '"+find+"' :",found.key," => ",found.value)

print("\nTree data :",tree.to_tuple())
print("\nTree key,value pair data :",tree.list_all())
print("\nIn order traversal :",tree.traverse('in'))
print("\nPre order traversal :",tree.traverse('pre'))
print("\nPost order traversal :",tree.traverse('post'))

print("\n\n\nDisplay :")
tree.display()