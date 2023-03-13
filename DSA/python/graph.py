class Graph:
	def __init__(self, num_nodes,edges):
		self.num_nodes = num_nodes
		self.data = [[] for _ in range(num_nodes)]
		for n1,n2 in edges:
			self.data[n1].append(n2)
			self.data[n2].append(n1)

	def display(self):
		for n,neibours in enumerate(self.data):
			print(n,":",neibours)

	def addEdge(self,n1,n2):
		self.data[n1].append(n2)
		self.data[n2].append(n1)

	def removeEdge(self,n1,n2):
		self.data[n1].remove(n2)
		self.data[n2].remove(n1)

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

		stack.append(root)
		discovered[root] = True
		result = []

		while len(stack)>0:
			current = stack.pop()
			discovered[current] = True
			result.append(current)
			for node in self.data[current]:
				if not discovered[node]:
					stack.append(node)
		return result



graph1 = Graph(5,[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)])
print("Initial graph:")
graph1.display()

graph1.addEdge(0,3)
print("\n\nAdded edge => 0,3:")
graph1.display()

graph1.removeEdge(0,3)
print("\n\nRemoved edge => 0,3:")
graph1.display()

print("\n\nBFS:")
queue,distance,parent = graph1.bfs(3)
print('Traversal : ',queue,'\nDistance : ',distance,'\nParent : ',parent)

print("\n\nDFS:")
queue= graph1.dfs(3)
print('Traversal : ',queue)