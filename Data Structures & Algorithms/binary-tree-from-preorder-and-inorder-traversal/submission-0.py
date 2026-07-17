# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # given the preorder and inorder list, ouput the tree built on that

        # base case
        if not preorder:
            return None

        # current logic:
        # find the root of this tree, and its leftChild and rightChild
        for i, val in enumerate(inorder):
            if val == preorder[0]:
                leftNum = i
                leftRange = (0, i) # including 0 but not i
                rightNum = len(inorder)-i-1
                rightRange = (i+1, len(inorder)) # including i+1 but not len(inorder)
                break

        # subproblem
        leftTree = self.buildTree(preorder[1:1+leftNum], inorder[leftRange[0]:leftRange[1]])
        rightTree = self.buildTree(preorder[1+leftNum:len(preorder)], inorder[rightRange[0]:rightRange[1]])

        root = TreeNode(preorder[0],leftTree, rightTree)

        return root