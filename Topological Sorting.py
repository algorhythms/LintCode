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


    def topSort(self, graph):
        """
        dfs
        1. pick an unvisited node
        2. add neighbors and sub-neighbors to result first
        3. then add the node itself to the result
        4. until all nodes are visited

        :param graph: A list of Directed graph node
        :return: graph
        """
        unvisited = set(graph)

        ret = []
        while unvisited:
            cur = unvisited.copy().pop()
            self.dfs(cur, unvisited, ret)

        return ret

    def dfs(self, cur, unvisited, ret):
        """

        :param cur: cur must be UNVISITED (pre-check)
        :param unvisited:
        :param ret:
        :return:
        """
        for nbr in cur.neighbors:
            if nbr in unvisited:
                self.dfs(nbr, unvisited, ret)
        ret.push(0, cur)  # notice the insertion order
        unvisited.remove(cur)
