# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        HeightOrBalanced = self.getHeightOrBalanced(root)
        if HeightOrBalanced == -1:
            return False
        else:
            return True

    def getHeightOrBalanced(self, root: Optional[TreeNode]) -> int:
        # base case
        if not root:
            return 0

        # subproblem
        leftHeight = self.getHeightOrBalanced(root.left)
        rightHeight = self.getHeightOrBalanced(root.right)

        # current logic
        if leftHeight == -1 or rightHeight == -1:
            return -1
        elif abs(leftHeight-rightHeight) <= 1:
            return max(leftHeight, rightHeight)+1
        else:
            return -1
        