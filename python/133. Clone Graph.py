"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# https://www.youtube.com/watch?v=mQeF6bN8hMk
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloneMap = {}

        def dfs_clone(node):
            if node in cloneMap:
                return cloneMap[node]

            copy = Node(node.val)
            cloneMap[node] = copy
            for neighborNode in node.neighbors:
                copy.neighbors.append(dfs_clone(neighborNode))
            return copy

        return dfs_clone(node) if node else None