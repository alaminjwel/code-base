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