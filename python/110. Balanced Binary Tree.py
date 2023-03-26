class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def helper(node):
            if node is None:
                return 0
            lft,rgt = helper(node.left),helper(node.right)
            if abs(lft-rgt)>1:
                self.bal = False
            return 1+max(lft,rgt)

        helper(root)
        return self.bal