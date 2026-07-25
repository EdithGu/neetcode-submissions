"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # queue: store the nodes we have found but havent processed yet
        queue = collections.deque()
        
        # map: store {original: clone} nodes pair
        oldToClone = {}

        queue.append(node)
        clone = Node(node.val)        
        oldToClone[node] = clone

        while queue:
            # only process the out-degree of current node
            curr = queue.popleft()
            curr_clone = oldToClone[curr]

            for nei in curr.neighbors:
                # we find a new unprocessed neighbor
                if nei not in oldToClone:
                    queue.append(nei)
                    nei_clone = Node(nei.val)
                    oldToClone[nei] = nei_clone
                else:
                    nei_clone = oldToClone[nei]

                # connect the cur_clone to its neighbor
                curr_clone.neighbors.append(nei_clone)
        
        return oldToClone[node]






