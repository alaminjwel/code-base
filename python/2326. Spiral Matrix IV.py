# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        left,right=0,n
        top,bottom=0,m
        while head and left<right and top<bottom:
           
            for i in range(left,right):                
                if not head:
                    break
                matrix[top][i]=head.val
                head = head.next
            top+=1

            for i in range(top,bottom):                
                if not head:
                    break
                matrix[i][right-1]=head.val
                head = head.next
            right-=1

            if not (left<right and top<bottom):
                break

            for i in range(right-1,left-1,-1):                
                if not head:
                    break
                matrix[bottom-1][i]=head.val
                head = head.next                    
            bottom-=1

            for i in range(bottom-1,top-1,-1):                
                if not head:
                    break
                matrix[i][left]=head.val
                head = head.next
            left+=1

        return matrix

node1 = ListNode(3)
node2 = ListNode(0)
node3 = ListNode(2)
node4 = ListNode(6)
node5 = ListNode(8)
node6 = ListNode(1)
node7 = ListNode(7)
node8 = ListNode(9)
node9 = ListNode(4)
node10 = ListNode(2)
node11 = ListNode(5)
node12 = ListNode(5)
node13 = ListNode(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13
node13.next = None


m = 9
n = 6
values = [995,348,36,516,333,627,248,422,13,225,764,311,405,695,698,83,145,783,478]

m = 3
n = 5
values = [3,0,2,6,8,1,7,9,4,2,5,5,0]

# convert list to linked list
head = ListNode(values[0])
node = head
for val in values[1:]:
    node.next = ListNode(val)
    node = node.next

obj = Solution()
print(obj.spiralMatrix(m,n,head))