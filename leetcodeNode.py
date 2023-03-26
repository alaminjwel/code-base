from typing import List
from typing import Optional
import queue

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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node.left is None and node.right is None:
                return True if node.val==1 else False
            lft,rgt = helper(node.left),helper(node.right)
            if node.val==2:
                return lft or rgt
            if node.val==3:
                return lft and rgt
        return helper(root)



node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
node4 = TreeNode(None)
node5 = TreeNode(None)
node6 = TreeNode(0)
node7 = TreeNode(1)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

obj = Solution()
print(obj.evaluateTree(node1))
# print(node1.display())
