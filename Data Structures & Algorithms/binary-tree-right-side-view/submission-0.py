# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        if root:
            queue.append(root)
        res = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                popped_ele = queue.popleft()
                if i == level_size - 1:
                    res.append(popped_ele.val)
                if popped_ele.left:
                    queue.append(popped_ele.left)
                if popped_ele.right:
                    queue.append(popped_ele.right)

        return res