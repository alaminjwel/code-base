from typing import List
from typing import Optional
from collections import deque

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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        maxLevel=1
        level=1
        maxSum=float('-inf')
        while q:
            s=0
            for _ in range(len(q)):
                node=q.popleft()
                s+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if s>maxSum:
                maxSum=s
                maxLevel=level
            level+=1
        return maxLevel

        


node1 = TreeNode(1)
node2 = TreeNode(7)
node3 = TreeNode(0)
node4 = TreeNode(7)
node5 = TreeNode(-8)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
# node1.display()

obj = Solution()
res = obj.maxLevelSum(node1)
print(res)
