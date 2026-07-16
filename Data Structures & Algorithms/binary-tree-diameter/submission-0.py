# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        _ = self.getDepth(root, res)
        return res[0]

    def getDepth(self, root:TreeNode, maxDiameter:List[int]) -> int:
        # base case
        if not root:
            return 0

        # subproblem
        leftHeight = self.getDepth(root.left, maxDiameter)
        rightHeight = self.getDepth(root.right, maxDiameter)

        # current level
        maxDiameter[0] = max(maxDiameter[0], leftHeight+rightHeight)
        return max(leftHeight, rightHeight)+1
        