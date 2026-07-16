# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = self.hasPQOrLCAOrNothin(root, p, q)
        return res

    def hasPQOrLCAOrNothin(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode')  -> 'Optional[TreeNode]':
        # base case
        if not root:
            return None

        # current logic
        if root.val == p.val or root.val == q.val:
            return root

        # subproblem
        left = self.hasPQOrLCAOrNothin(root.left, p, q)
        right = self.hasPQOrLCAOrNothin(root.right, p, q)

        if not left and not right:
            return None
        elif left and right:
            return root
        elif left:
            return left
        else:
            return right
