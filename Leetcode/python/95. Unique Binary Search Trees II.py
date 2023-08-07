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
        