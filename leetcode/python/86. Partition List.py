from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
   def partition(self, head: ListNode, x: int) -> ListNode:
       left,right = ListNode(0),ListNode(0)
       l,r = left,right
       
       while head:
           if head.val < x:
               l.next = head
               l = l.next
           else:
               r.next = head
               r = r.next
           head = head.next
           
       l.next = right.next
       r.next = None
       displayLinkedList(left.next)
       return left.next




def generateLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def displayLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

arr = [1,4,3,2,5,2]
linkedList = generateLinkedList(arr)
# displayLinkedList(linkedList)

obj = Solution()
res = obj.partition(linkedList,3)
print(res)