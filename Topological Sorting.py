"""
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A-->B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Note
You can assume that there is at least one topological order in the graph.
"""
__author__ = 'Danyang'
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def topSort_error(self, graph):
        """

        :param graph:
        :return: graph
        """
        node2neighbors = {}
        for node in graph:
            node2neighbors[node] = set(node.neighbors)

        # error, edge is transitive
        def cmp(a, b):
            if a in node2neighbors[b]:
                return 1
            if b in node2neighbors[a]:
                return -1
            return 0

        graph.sort(cmp=cmp)
        return graph

    def topSort_normal(self, graph):
        """
        Without dfs/bfs

        1. get all the predecessors of each node
        2. pop a node without a predecessors and add it to result list
        3. update the predecessors of each node

        :param graph: A list of Directed graph node
        :return: graph
        """
        pi = {}
        for node in graph:
            pi[node] = set()

        for node in graph:
            for nbr in node.neighbors:
                pi[nbr].add(node)

        ret = []
        while graph:
            i = 0
            while i<len(graph):
                if len(pi[graph[i]])!=0:
                    i += 1
                else:
                    ret.append(graph[i])
                    for nbr in graph[i].neighbors:
                        if graph[i] in pi[nbr]:
                            pi[nbr].remove(graph[i])
                    graph.pop(i)
                    # break  # no break, otherwise TLE
                    # should continue searching the next node rather than break
        return ret


    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    def topSort(self, graph):
        """
        dfs
        1. pick an unvisited node
        2. add neighbors and sub-neighbors first
        3. until all nodes are visited

        :param graph: A list of Directed graph node
        :return: graph
        """
        status = {}
        for node in graph:
            status[node] = Solution.UNVISITED


        ret = []
        while True:
            cur = self.get_unvisited(status, graph)
            if not cur: break
            self.dfs(cur, status, ret)

        return ret

    def dfs(self, cur, status, ret):
        """

        :param cur: cur must be UNVISITED (pre-check)
        :param status:
        :param ret:
        :return:
        """
        status[cur] = Solution.VISITING
        for nbr in cur.neighbors:
            if status[nbr]==Solution.VISITING:
                raise Exception("Cyclic Graph")
            elif status[nbr]==Solution.UNVISITED:
                self.dfs(nbr, status, ret)
        ret.insert(0, cur)  # insert order
        status[cur] = Solution.VISITED


    def get_unvisited(self, status, graph):
        for node in graph:
            if status[node]==Solution.UNVISITED:
                return node
        return None
