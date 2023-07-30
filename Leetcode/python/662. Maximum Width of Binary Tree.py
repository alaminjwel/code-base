from typing import List
from typing import Optional
import queue
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([(root,1,0)]) # node,num,level
        prevLevel,prevNum = 0,1
        while q:
            node,num,level = q.popleft()
            if level>prevLevel:
                prevLevel = level
                prevNum = num
            res = max(res,num - prevNum + 1)
            if node.left:
                q.append((node.left, 2*num, level+1))
            if node.right:
                q.append((node.right, 2*num+1, level+1))
        return res



node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2)
node4 = TreeNode(5)
node5 = TreeNode(3)
node6 = TreeNode(None)
node7 = TreeNode(9)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

obj = Solution()
print(obj.widthOfBinaryTree(node1))
# print(node1.display())
