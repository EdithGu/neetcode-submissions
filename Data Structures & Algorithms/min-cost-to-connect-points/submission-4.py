class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minHeap + visited set
        
        
            
           
                # vistited: skip
                

        # tc: ElogE. sc:O(E)

        minHeap = []
        visited = set()
        total_num = len(points)
        total_cost = 0

        # start from (0,0): add to minheap
        heapq.heappush(minHeap, (0, points[0]))

        # pop out element from minHEap + make sure stll have unvisted set:
        while minHeap and len(visited) != total_num:
            # means the minimum cost to connect this point at the current stage
            cur_cost, cur_point = heapq.heappop(minHeap)

            # check whether visit this point:
            if tuple(cur_point) in visited:
                continue
            # unvisited: mark visited, update total cost, 
            total_cost += cur_cost
            visited.add(tuple(cur_point))
            if len(visited) == total_num:
                return total_cost

            # span only visited neighbor nodes and its according edge cost to minHeap
            for nei in points:
                if tuple(nei) in visited:
                    continue
                nei_cost = abs(nei[0]-cur_point[0]) + abs(nei[1]-cur_point[1])
                heapq.heappush(minHeap, (nei_cost, nei))

        return total_cost
















