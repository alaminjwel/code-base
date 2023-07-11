# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head2 = dummy

        while head2.next and head2.next.next:
            l = head2.next
            r = head2.next.next
            head2.next = r
            l.next = r.next
            r.next = l
            head2 = head2.next.next

        return dummy.next