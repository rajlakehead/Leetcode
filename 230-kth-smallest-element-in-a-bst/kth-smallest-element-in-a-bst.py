# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = [0]
        ans = [0]


        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            n[0] += 1
            if n[0] == k:
                ans[0] = root.val
                return
            dfs(root.right)
        dfs(root)
        return ans[0]
        
        