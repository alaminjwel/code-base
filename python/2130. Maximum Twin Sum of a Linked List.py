from typing import List
from typing import Optional
import queue
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # First we find the list length
        head2=head
        length=0
        while head2:
            length+=1
            head2=head2.next

        i=0
        maximum=0
        firstSlice=[] # Will contain values of first half of the list
        while head:
            if i<length/2: # This is first half
                firstSlice.append(head.val)
            else: # This is last half
                # firstSliceItem looks like [5,4],so we pick our value by popping
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