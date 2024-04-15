# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root, number):
            if not root:
                return
            if not root.left and not root.right:
                number += str(root.val)
                res.append(int(number))
                return
            
            number += str(root.val)
            dfs(root.left, number)
            dfs(root.right, number)
        dfs(root, "")
        return sum(res)