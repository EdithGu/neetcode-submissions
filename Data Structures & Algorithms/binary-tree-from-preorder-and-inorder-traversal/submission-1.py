# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderHashmap = {} # {nodeValue: index}
        for i, val in enumerate(inorder):
            inorderHashmap[val] = i

        tree = self.build(preorder, inorder, inorderHashmap, 0, len(inorder)-1, [0] ) 
        return tree

    def build(self, preorder:List[int], inorder:List[int], inorderhashmap:Dict, left:int, right:int, pre_idx:List[int]) -> Optional[TreeNode]:
        # build a tree within left and right range in the inorder list

        # base case
        if left > right:
            return None

        # current level logic
        # in the left-right range, find the root and its left, right subtree
        # root must be preorder[left]
        # get root's index from hashmap, the ele on its left side form left tree, and ele on its right side form right tree

        root = preorder[pre_idx[0]]
        pre_idx[0] += 1
        rootIndexInorder = inorderhashmap[root]

        # subproblem
        leftTree = self.build(preorder, inorder, inorderhashmap, left, rootIndexInorder-1, pre_idx)
        rightTree = self.build(preorder, inorder, inorderhashmap, rootIndexInorder+1, right, pre_idx)

        tree = TreeNode(root, leftTree, rightTree)
        return tree



