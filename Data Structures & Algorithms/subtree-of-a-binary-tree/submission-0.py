# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #signature: whether tree subRoot is a subtree of tree root

        # base case
        if not root:
            return False

        # subProblem
        isSubOfLeft = self.isSubtree(root.left, subRoot)
        isSubOfRight = self.isSubtree(root.right, subRoot)

        # currentLevel
        if isSubOfLeft or isSubOfRight:
            return True
        else:
            return self.isSame(root, subRoot)

    def isSame(self, root:Optional[TreeNode], subRoot:Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False

        isLeftSame = self.isSame(root.left, subRoot.left)
        isRightSame = self.isSame(root.right, subRoot.right)

        if not isLeftSame or not isRightSame:
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return True








