class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # build graph
        graph = [[] for _ in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = set()
        hasCycle = [False]
        self.dfs(0, visited, graph, -1, hasCycle)

        if hasCycle[0] == True:
            return False
        if len(visited) != n:
            return False

        return True


    def dfs(self, node:int, visited:set, graph:List[List[int]], prev:int, hasCycle:[bool]) -> None:
        if node in visited:
            hasCycle[0] = True
            return

        visited.add(node)
        for nei in graph[node]:
            if nei == prev:
                continue

            self.dfs(nei, visited, graph, node, hasCycle)


