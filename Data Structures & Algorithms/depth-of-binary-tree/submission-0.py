# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root :
            return 0

        # sub-problem:
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # cur level
        return max(left_depth, right_depth) + 1