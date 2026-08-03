class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build graph: each node will record outgoing neis in lexicographical order
        graph = defaultdict(list)
        for _from, _to in tickets:
            nei = graph[_from]
            nei.append(_to)

        print(graph)


        for node, nei in graph.items():
            nei.sort() 
        print(graph)


        # start from JFK, do  dfs
        res = []
        self.dfs(graph, "JFK", res)

        # reverse the list
        res.reverse()

        return res

    def dfs(self, graph:dict, node:str, res:List) -> None:
        # at each level: traverse all its neighbor, remove the edge
        print(f"{node}:{graph[node]}")
        while graph[node]:
            nei = graph[node][0]
            graph[node].remove(nei)
            # do the same dfs logic to that neighbor
            self.dfs(graph, nei, res)

        # after we traverse all neibors of a node, put the node into res list
        res.append(node)
        return



# JFK:[]
# HOU:[]
# SEA:[]


# res: [JFK, SEA, JFK, HOU, JFK]
# reversed: [JFK, HOU, JFK, SEA, JFK]

# enter JFK:
#     enter HOU :
#         enter JFK:
#             enter SEA:
#                 enter JFK:
#                 leave JFK
#             leave SEA
#         leave JFK
#     leave HOU
# leave JFK

# TC:
# O(V+E)

# SC:
# O(V+E)

    




        