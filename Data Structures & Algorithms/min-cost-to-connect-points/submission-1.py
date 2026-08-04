class Solution:

    class union_find:
        def __init__(self, points: List[List[int]]):
            self.parents = {tuple(point):point for point in points}
            self.rank = {tuple(point):1 for point in points}

        def checkCycle(self, node1:List, node2:List):
            r1, r2 = self.find(node1), self.find(node2)
            if self.isSame(r1, r2):  
                return (True, r1, r2)
            else:
                return (False, r1, r2)

        def connect(self, node1:List, node2:List, r1:List, r2:List):
            if self.rank[tuple(r1)] > self.rank[tuple(r2)]:
                # r1 will be the parent
                self.parents[tuple(r2)] = r1
                del self.rank[tuple(r2)]
            elif self.rank[tuple(r1)] < self.rank[tuple(r2)]:
                # r2 will be the parent
                self.parents[tuple(r1)] = r2
                del self.rank[tuple(r1)]
            else:
                self.parents[tuple(r2)] = r1
                del self.rank[tuple(r2)]
                self.rank[tuple(r1)] += 1

        def isSame(self, node1:List, node2:List) -> bool:
            if node1[0] == node2[0] and node1[1] == node2[1]:
                return True
            else :
                return False

        def find(self, node:List) -> List:
            while not self.isSame(self.parents[tuple(node)], node):
                node = self.parents[tuple(node)]
            return node






    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal
        n = len(points)

        # put each possible edge into a minHeap
        minHeap = []
        for i in range(n):
            node1 = points[i]
            for j in range(i+1, n):
                node2 = points[j]
                cost = abs(node1[0]-node2[0]) + abs(node1[1]-node2[1])
                heapq.heappush(minHeap, (cost, node1, node2))

        unionFind = self.union_find(points)
        edge_count = 0
        total_cost = 0
        # popped out a local minimum cost edge, 
        while minHeap:
            cost, node1, node2 = heapq.heappop(minHeap)

            # check whether node1 and node2 already in the same part
            causeCycle, r1, r2 = unionFind.checkCycle(node1, node2)

            # if not, count current edges, if have n-1 edges return here. and 
            if not causeCycle:
                edge_count += 1
                total_cost += cost
                if edge_count == n-1:
                    return total_cost
                
                # connet these two points with union find 
                # update node1 and node2 parents and its root tree
                unionFind.connect(node1, node2, r1, r2)


        # if yes, then connecting these tow nodes will lead cycle, then skip it
        return total_cost

        