# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorderList = []
        self.proOrderPlusPrint(root, preorderList)
        return ','.join(str(s) for s in preorderList)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preOrderList = data.split(',')
        index = [0]
        root = self.constructTree(preOrderList, index)
        return root

    # preorder the tree and put each node including null into a list
    def proOrderPlusPrint(self, root:TreeNode, preorderList: List) -> None:
        # base case
        if not root:
            preorderList.append(None)
            return

        # current logic
        preorderList.append(root.val)

        # subproblem
        self.proOrderPlusPrint(root.left, preorderList)
        self.proOrderPlusPrint(root.right, preorderList)

    def constructTree(self, preOrderList:List, index:List[int]) -> Optional[TreeNode]:
        # base case
        if index[0] == len(preOrderList):
            return
        if preOrderList[index[0]] == 'None':
            index[0] += 1
            return None

        # current logic
        root = TreeNode(val = int(preOrderList[index[0]]))
        index[0] += 1

        # subproblem
        left = self.constructTree(preOrderList, index)
        right = self.constructTree(preOrderList, index)

        root.left = left
        root.right = right

        return root        

