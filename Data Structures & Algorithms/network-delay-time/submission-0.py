class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weighted_graph = [[] for _ in range(n+1)]
        for _from, _to, _time in times:
            weighted_graph[_from].append((_to, _time))
        print(weighted_graph)

        minHeap = []    #(cost, node)
        heapq.heappush(minHeap, (0, k))
        visited = set()

        while minHeap:
            cur = heapq.heappop(minHeap)
            if cur[1] in visited:
                continue
            visited.add(cur[1])
            if len(visited) == n:
                return cur[0]
            for nei in weighted_graph[cur[1]]:
                if nei[0] in visited:
                    continue
                heapq.heappush(minHeap,(cur[0]+nei[1], nei[0]))

        return -1

            






