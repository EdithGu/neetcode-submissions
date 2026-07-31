class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph
        # nodes:[outdgree]. node is the prerequisite class
        graph = [[] for _ in range(numCourses)]
        for _to, _from in prerequisites:
            graph[_from].append(_to)
        print(graph)


        # do dfs to each node
        # core logic: after processing the current node's neighbor, writed down current node
        # but if at the cur path we meet a same node -> has cycle
        # if we meet a already visited node -> this node has already been processed, skip it
        visited = set()
        class_sequence = []
        hasCycle = [False]

        for i in range(numCourses):
            curPath = set()
            self.dfs(i, curPath, visited, class_sequence, hasCycle, graph)
            if hasCycle[0] == True:
                return []

        class_sequence.reverse()
        print(class_sequence)
        return class_sequence


    def dfs(self, node:int, curPath:set, visited:set, class_sequence:List, hasCycle:[bool], graph:List[List]) -> None:
        if node in curPath:
            # detect a cycle
            hasCycle[0] = True
            return
        if hasCycle[0] == True or node in visited:
            return


        # a valid unvisited node
        curPath.add(node)
        visited.add(node)
        for nei in graph[node]:
            self.dfs(nei, curPath, visited, class_sequence, hasCycle, graph)
            if hasCycle[0] == True:
                return
        class_sequence.append(node)
        curPath.remove(node)

        