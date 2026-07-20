# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]
        self.maxPathSumFromLeafToRoot(root, maxSum)

        return maxSum[0]

    def maxPathSumFromLeafToRoot(self, root: TreeNode, maxSum:List[int]) -> int:
        # base case
        if not root:
            return 0

        # sub-problem
        leftMaxPathSumFromLeafToRoot = self.maxPathSumFromLeafToRoot(root.left, maxSum)
        rightMaxPathSumFromLeafToRoot = self.maxPathSumFromLeafToRoot(root.right, maxSum)

        # current logic
        left = max(leftMaxPathSumFromLeafToRoot, 0)
        right = max(rightMaxPathSumFromLeafToRoot, 0)
        cur = root.val + left + right
        print(f"current node: {root.val}")
        print(f"left pathSum: {left}")
        print(f"right pathSum: {right}")
        print(f"maxSum: {maxSum[0]} \n")
        maxSum[0] = max(cur, maxSum[0])

        return root.val + max(left, right)
        