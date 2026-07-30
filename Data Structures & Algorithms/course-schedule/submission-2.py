class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first build graph
        # each node records its outdegree
        graph = [[] for _ in range(numCourses)]

        for _to, _from in prerequisites:
            graph[_from].append(_to)


        
        visited = set()
        hasCycle = [False]
        # dfs: starting from input node, is there a cyle?
        for i in range(numCourses):
            if hasCycle[0] == True:
                return False
            curPath = []
            self.dfs(i, curPath, visited, graph, hasCycle)

        return not hasCycle[0]


    def dfs(self, node:int, curPath:List[int], visited:set, graph:List[List], hasCycle:[bool]):
        # base case
        if hasCycle[0] == True:
            return
        if node in curPath:
            hasCycle[0] = True
            curPath.append(node)
            # find the nodes in the cycle
            cycle = self.findCycleNodes(curPath)
            print(cycle)
            curPath.pop()
            return 
        if node in visited:
            return

        visited.add(node)
        curPath.append(node)
        for outdegree in graph[node]:
            self.dfs(outdegree, curPath, visited, graph, hasCycle)
        curPath.pop()

    def findCycleNodes(self, curPath) -> List:
        entry = curPath[-1]
        for i in range(len(curPath)):
            if curPath[i] == entry:
                return curPath[i:-1]







