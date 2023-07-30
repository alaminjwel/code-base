from typing import List
from typing import Optional
import queue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        head2 = head;
        while head2:
             length+=1
             head2=head2.next

        i,l,r=0,-1,-1
        head2 = head;
        while head2 and i<length:
            if i==k-1:
                l=head2.val
            if i==length-k:
                r=head2.val
            i+=1
            head2=head2.next

        if l<0 or r<0:
            return head

        i=0
        head2 = head;
        while head2 and i<length:
            if i==k-1:
                head2.val=r
            if i==length-k:
                head2.val=l
            i+=1
            head2=head2.next
        return head

values = [7,9,6,6,7,8,3,0,9,5]
# convert list to linked list
head = ListNode(values[0])
node = head
for val in values[1:]:
    node.next = ListNode(val)
    node = node.next
obj = Solution()
print(obj.swapNodes(head,5))