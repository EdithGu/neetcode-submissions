# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, root:Optional[TreeNode], left:int, right:int) -> bool:
        # whether the tree 'root' is a valid BST under the contraint (left, right)
        
        # base case
        if not root:
            return True

        # current logic
        if root.val >= right or root.val <= left:
            return False

        # subproblem
        leftValid = self.isValid(root.left, left, root.val)
        rightValid = self.isValid(root.right, root.val, right)

        if not leftValid or not rightValid:
            return False
        else:
            return True
        