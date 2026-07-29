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
            return node

        queue = collections.deque() # hepl tho traverse all nodes in graph
        visited = {} # record all visited nodes

        queue.append(node)
        # make a copy 
        copy = Node(node.val)
        # add in map
        visited[node] = copy

        while queue:
            cur = queue.popleft()
            cur_copy = visited[cur]

            # add its neighbors
            for nei in cur.neighbors:
                if nei not in visited:
                    queue.append(nei)
                    nei_copy = Node(nei.val)
                    visited[nei] = nei_copy
                else:
                    nei_copy = visited[nei]

                cur_copy.neighbors.append(nei_copy)

        return visited[node]

        