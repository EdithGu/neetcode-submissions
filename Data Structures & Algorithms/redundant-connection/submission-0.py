class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = {i:i for i in range(1, n+1)}
        rank = {i:1 for i in range(1, n+1)}

        for v1, v2 in edges:
            r1, r2 = self.find(v1, parents), self.find(v2,parents)
            if r1 == r2:
                # we find the edge causing the cycle
                return [v1, v2]

            # connect these two part
            if rank[r1] > rank[r2]:
                # r1 will be the parent
                parents[r2] = r1
                rank.pop(r2, None)
            elif rank[r1] < rank[r2]:
                parents[r1] = r2
                rank.pop(r1, None)
            else:
                parents[r2] = r1
                rank.pop(r2, None)
                # update r1's rank
                rank[r1] += 1

    def find(self, node:int, parents:set) -> int:
        while node != parents[node]:
            node = parents[node]
        return node


