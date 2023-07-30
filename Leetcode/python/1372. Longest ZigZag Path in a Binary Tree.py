# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/solutions/3433173/python3-solution/?orderBy=most_votes&languageTags=python3
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans=0
        stack=[(root,0,None)]
        while stack:
            node,n,left=stack.pop()
            if node:
                ans=max(ans,n)
                stack.append((node.left,1 if left else n+1,1))
                stack.append((node.right,n+1 if left else 1,0))

        return ans  