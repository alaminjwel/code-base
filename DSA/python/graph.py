class Graph:
	def __init__(self, num_nodes,edges,adjacencyMatrix=False):
		self.adjacencyMatrix=adjacencyMatrix  # tracking if we are using adjacencyMatrix or not
		self.num_nodes = num_nodes
		if adjacencyMatrix:  # adjacency matix representation of graph
			self.data = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
			for n1,n2 in edges:
				self.data[n1][n2] = 1
				self.data[n2][n1] = 1
		else:  # adjacency representation of graph
			self.data = [[] for _ in range(num_nodes)]
			for n1,n2 in edges:
				self.data[n1].append(n2)
				self.data[n2].append(n1)

	def display(self):
		if self.adjacencyMatrix:  # adjacencyMatrix representation of graph
			for i in range(len(self.data)):
				print(self.data[i])
		else:  # adjacency representation of graph
			for n,neibours in enumerate(self.data):
				print(n,":",neibours)

	def addEdge(self,n1,n2):
		if self.adjacencyMatrix:  # adjacencyMatrix representation of graph
			self.data[n1][n2] = 1
			self.data[n1][n2] = 1
		else:  # adjacency representation of graph
			self.data[n1].append(n2)
			self.data[n2].append(n1)

	def removeEdge(self,n1,n2):
		if self.adjacencyMatrix:  # adjacencyMatrix representation of graph
			self.data[n1][n2] = 0
			self.data[n1][n2] = 0
		else:  # adjacency representation of graph
			self.data[n1].remove(n2)
			self.data[n2].remove(n1)


graph1 = Graph(5,[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)])
print("Initial graph:")
graph1.display()

graph1.addEdge(0,3)
print("\n\nAdded edge => 0,3:")
graph1.display()

graph1.removeEdge(0,3)
print("\n\nRemoved edge => 0,3:")
graph1.display()