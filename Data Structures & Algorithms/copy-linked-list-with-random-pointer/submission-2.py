"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        nodeMap = dict() # originalNode(val, next, random): newNode(val, next, random )

        cur = head 
        while cur:
            # check whether the current node already exist
            curNewNode = self.get_or_create(cur,nodeMap)
            
            cur_next = self.get_or_create(cur.next,nodeMap)
            curNewNode.next = cur_next
            cur_random = self.get_or_create(cur.random,nodeMap)
            curNewNode.random = cur_random
            
            cur = cur.next

        return nodeMap[head]

    def get_or_create(self, original_node:'Optional[Node]', nodemap:dict) -> 'Optional[Node]':
        
        if original_node == None:
            return None
        if original_node in nodemap:
            # if created, directly return
            return nodemap[original_node]
        else:
            #create if not existed
            newNode = Node(original_node.val)
            nodemap[original_node] = newNode
            return newNode


