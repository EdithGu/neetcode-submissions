# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # assume k is valid
        stack = collections.deque()

        while root:
            stack.append(root)
            root = root.left

        while stack:
            popped = stack.pop()
            if k == 1:
                return popped.val
            k -= 1

            # add the right childe into stack
            cur = popped.right
            while cur:
                stack.append(cur)
                cur = cur.left