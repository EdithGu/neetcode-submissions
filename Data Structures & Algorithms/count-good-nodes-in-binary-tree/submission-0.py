# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = [0]
        maxAlongPath = float('-inf')
        self.isGood(root, maxAlongPath, counter)

        return counter[0]

    def isGood(self, root:TreeNode, maxAlongPath:int, counter:List[int]) -> None:
        # only process the current root, whether it's good 
        # then same logic to process its child nodes
        # carry a global counter
        
        # base case
        if not root:
            return

        # current logic
        if root.val >= maxAlongPath:
            print(f"maxAlongPath:{maxAlongPath}, root:{root.val}")
            counter[0] += 1
            maxAlongPath = root.val

        # subproblem
        self.isGood(root.left, maxAlongPath, counter)
        self.isGood(root.right, maxAlongPath, counter)