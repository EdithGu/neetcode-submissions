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
        
        visited = {}
        copy = self.dfs(node, visited)
        return copy

    def dfs(self, node:Optional['Node'], visited:dict) -> 'Node':
        # base case
        # node in visited_map means it has been seen before
        # maybe the node has been processed fully or the node only half processed
        # but it doesnt matter
        # we just return this copy_node to it's parent caller to let its parent_copy_node add its neighbor
        if node in visited:
            return visited[node]

        # at each level, we are processing a new unseen node
        # create its copy, and point the copy_node to all its copy_neibor
        copy = Node(node.val)
        visited[node] = copy
        for nei in node.neighbors:
            nei_copy = self.dfs(nei, visited)
            copy.neighbors.append(nei_copy)

        return copy