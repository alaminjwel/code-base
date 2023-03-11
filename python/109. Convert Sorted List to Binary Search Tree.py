# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        headList = []
        while head:
            headList.append(head.val)
            head = head.next

        def make_balanced_bst(lo=0,hi=None):
            if hi is None:
                hi = len(headList)-1
            if lo>hi:
                return None
            mid = (hi+lo)//2
            root = TreeNode(headList[mid])
            root.left = make_balanced_bst(lo,mid-1)
            root.right = make_balanced_bst(mid+1,hi)
            return root
        return make_balanced_bst()