# Farthest Nodes
# Have the function FarthestNodes(strArr) read strArr which will be an array of hyphenated letters representing paths between those two nodes. For example: ["a-b","b-c","b-d"] means that there is a path from node a to b (and b to a), b to c, and b to d. Your program should determine the longest path that exists in the graph and return the length of that path. So for the example above, your program should return 2 because of the paths a-b-c and d-b-c. The path a-b-c also means that there is a path c-b-a. No cycles will exist in the graph and every node will be connected to some other node in the graph.
# Examples
# Input: ["b-e","b-c","c-d","a-b","e-f"]
# Output: 4
# Input: ["b-a","c-e","b-c","d-c"]
# Output: 3

from collections import defaultdict
def FarthestNodes(strArr):
	edges = defaultdict(list)
	nodes = set()
	for e in strArr:
		s,d = e.split('-')
		edges[s].append(d)
		edges[d].append(s)
		nodes.add(s)
		nodes.add(d)

	maxLength = 0
	for node in nodes:
		stack = [(node, 0)]
		visited = set()
		while stack:
			currNode, currLength = stack.pop()
			maxLength = max(maxLength, currLength)
			visited.add(currNode)
			for neighbor in edges[currNode]:
				if neighbor not in visited:
					stack.append((neighbor, currLength + 1))
	return maxLength

print(FarthestNodes(["b-e","b-c","c-d","a-b","e-f"]))