class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ranks = {i:1 for i in range(n)}
        parents = {i:i for i in range(n)}

        for v1, v2 in edges:
            r1, r2 = self.find(v1, parents), self.find(v2, parents)
            if r1 == r2:
                continue


            if ranks[r1] > ranks[r2]:
                # r1 will be r2 parent
                # r2 will not be root anymore
                parents[r2] = r1
                ranks.pop(r2, None)
            elif ranks[r2] > ranks[r1]:
                parents[r1] = r2
                ranks.pop(r1, None)
            else:
                parents[r2] = r1
                ranks.pop(r2, None)
                ranks[r1] += 1

        return len(ranks)


    def find(self, node, parents) -> int:
        while parents[node] != node:
            node = parents[node]

        return node


