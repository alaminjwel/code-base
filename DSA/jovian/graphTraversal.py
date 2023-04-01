class Graph:
	def __init__(self,num_nodes,edges,directed=False,weignted=False):
		self.num_nodes = num_nodes
		self.directed = directed
		self.weignted = weignted
		self.data = [[] for _ in range(num_nodes)]
		self.weight = [[] for _ in range(num_nodes)]

		for edge in edges:
			if not self.weignted:
				n1,n2 = edge
				self.data[n1].append(n2)

				if not self.directed: # non-directed graphs have 2way edges
					self.data[n2].append(n1)

			else: # weighted graphs need weight mapping also
				n1,n2,w = edge
				self.data[n1].append(n2)
				self.weight[n1].append(w)

				if not self.directed: # non-directed graphs have 2way edges
					self.data[n2].append(n1)
					self.weight[n2].append(w)


	def display(self):
		if self.weignted:
			for n,(neibours,weights) in enumerate(zip(self.data,self.weight)):
				print(n,":",format(list(zip(neibours,weights))))
		for n,neibours in enumerate(self.data):
			print(n,":",neibours)


	def addEdge(self,n1,n2,w=None):
		if not self.weignted:
			self.data[n1].append(n2)
			if not self.directed: # non-directed graphs have 2way edges
				self.data[n2].append(n1)
		else: # weighted graphs need weight mapping also
			self.data[n1].append(n2)
			self.weight[n1].append(w)
			if not self.directed: # non-directed graphs have 2way edges
				self.data[n2].append(n1)
				self.weight[n2].append(w)


	def removeEdge(self,n1,n2):
		if not self.weignted:
			self.data[n1].remove(n2)
			if not self.directed: # non-directed graphs need 2way edges removed
				self.data[n2].remove(n1)
		else: # weighted graphs need weight to be removed also
			self.data[n1].remove(n2)
			self.weight[n1].remove(n2)
			if not self.directed: # non-directed graphs need 2way edges removed
				self.data[n2].remove(n1)
				self.weight[n2].remove(n1)	


	def bfs(self,root):
		queue = []
		discovered = [False] * len(self.data)
		distance = [None] * len(self.data)
		parent = [None] * len(self.data)

		queue.append(root)
		discovered[root] = True
		distance[root] = 0

		idx=0

		while idx<len(queue):
			current = queue[idx]
			idx+=1
			for node in self.data[current]:
				if not discovered[node]:
					queue.append(node)
					discovered[node] = True
					distance[node] = 1 + distance[current]
					parent[node] = current
		return queue,distance,parent


	def dfs(self,root):
		stack = []
		discovered = [False] * len(self.data)
		parent = [None] * len(self.data)

		stack.append(root)
		result = []
		cycle_count = 0

		while len(stack)>0:
			current = stack.pop()
			if not discovered[current]:
				discovered[current] = True
				result.append(current)
				for node in self.data[current]:
					if not discovered[node]:
						stack.append(node)
						parent[node] = current
					elif node!=parent[current]:
						cycle_count += 1
		return result,parent,cycle_count


# non-directed, not weighted
# graph = Graph(5,[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)])
# graph = Graph(9,[(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)])

# weighted
# graph = Graph(9,[(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)],weignted=True)

# directed
# graph = Graph(5,[(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)],directed=True)

# weighted directed
graph = Graph(6,[(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)],weignted=True,directed=True)

print("Initial graph:")
graph.display()

# graph.addEdge(0,3)
# print("\n\nAdded edge => 0,3:")
# graph.display()

# graph.removeEdge(0,3)
# print("\n\nRemoved edge => 0,3:")
# graph.display()

print("\n\nBFS:")
queue,distance,parent = graph.bfs(3)
print('Traversal : ',queue,'\nDistance : ',distance,'\nParent : ',parent)
if len(queue)==len(graph.data):
	print("Connected : Yes, all nodes are connected")
else:
	print("Connected : No, all nodes are not connected")

print("\n\nDFS:")
queue,parent,cycle_count = graph.dfs(3)
print('Traversal : ',queue,'\nParent : ',parent,'\nCycles : ',cycle_count)
