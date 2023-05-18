from typing import List
from typing import Optional
import queue
import math

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#     def display(self, space='\t', level=0):
#         if self is None:
#             print(space*level + ' ')
#             return

#         if self.left is None and self.right is None:
#             print(space*level + str(self.val))
#             return

#         TreeNode.display(self.right, space, level+1)
#         print(space*level + str(self.val))
#         TreeNode.display(self.left,space, level+1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head2=head
        length=0
        while head2:
            length+=1
            head2=head2.next

        i=0
        maximum=0
        firstSlice=[]
        while head:
            if i<length/2:
                firstSlice.append(head.val)
            else:
                firstSliceItem = firstSlice.pop()
                maximum=max(maximum,(firstSliceItem+head.val))
            head=head.next
            i+=1
        return maximum


values = [5,4,2,1]
# convert list to linked list
head = ListNode(values[0])
node = head
for val in values[1:]:
    node.next = ListNode(val)
    node = node.next

obj = Solution()
res = obj.pairSum(head)
print(res)

# while res:
#     print(res.val)
#     res=res.next

# print(node.display())
