from typing import List
from typing import Optional
import queue
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self, space='\t', level=0):
        if self is None:
            print(space*level + ' ')
            return

        if self.left is None and self.right is None:
            print(space*level + str(self.val))
            return

        TreeNode.display(self.right, space, level+1)
        print(space*level + str(self.val))
        TreeNode.display(self.left,space, level+1)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if node is None:
                return []
            return traverse(node.left)+[node.val]+traverse(node.right)
        values=traverse(root)
        ans=float("inf")
        for i in range(len(values)-1):
            ans=min(ans,values[i+1]-values[i])
        return ans


node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(6)
node4 = TreeNode(1)
node5 = TreeNode(3)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
# node1.display()

obj = Solution()
res = obj.getMinimumDifference(node1)
print(res)