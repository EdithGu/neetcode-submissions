# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        if root:
            queue.append(root)
        res = []

        while queue:
            num = len(queue)
            level_res = []
            print(queue)
            for i in range(num):
                poppedNode = queue.popleft()
                level_res.append(poppedNode.val)
                if poppedNode.left:
                    queue.append(poppedNode.left)
                if poppedNode.right:
                    queue.append(poppedNode.right)
            res.append(level_res)

        return res