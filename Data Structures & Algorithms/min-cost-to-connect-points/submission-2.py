class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # highlevel: 

        # detail:
        
        

            
            

        pq = []
        visited = set()
        total_cost = 0
        nodes_num = len(points)

        heapq.heappush(pq,(0, points[0]))
        while pq:
            # popped out pq_node:(edge_cost, node)
            cur_cost, cur_point = heapq.heappop(pq)

            # if the current node already be visited, skip
            if tuple(cur_point) in visited:
                continue

            # if it's an unseen node, meaning we are now connecting this node with the subgraph:
            # mark it as visited
            visited.add(tuple(cur_point))
            # update total cost
            total_cost += cur_cost
            # if all nodes have been visited, return here
            if len(visited) == nodes_num:
                return total_cost
            # span its unvisited neighbor nodes and the cost to connect these nodes
            for nei in points:
                if tuple(nei) in visited:
                    continue
                nei_cost = abs(nei[0]-cur_point[0]) + abs(nei[1]-cur_point[1])
                heapq.heappush(pq, (nei_cost, nei))


        if len(visited) == nodes_num:
            return total_cost





