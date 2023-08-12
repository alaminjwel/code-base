from typing import List
from typing import Optional
import queue
from collections import deque
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(l, r):
            if l > r:
                return [None]
            result = []
            for val in range(l, r + 1):
                left_trees = helper(l, val - 1)
                right_trees = helper(val + 1, r)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        result.append(root)
            return result
        
        return helper(1, n)
        


# node1 = TreeNode(1)
# node2 = TreeNode(7)
# node3 = TreeNode(0)
# node4 = TreeNode(7)
# node5 = TreeNode(-8)
# node1.left=node2
# node1.right=node3
# node2.left=node4
# node2.right=node5
# node1.display()

obj = Solution()
res = obj.generateTrees(3)
print(res)



# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# values = [5,4,2,1]
# # convert list to linked list
# head = ListNode(values[0])
# node = head
# for val in values[1:]:
#     node.next = ListNode(val)
#     node = node.next

# obj = Solution()
# res = obj.pairSum(head)
# print(res)

# while res:
#     print(res.val)
#     res=res.next

# print(node.display())
