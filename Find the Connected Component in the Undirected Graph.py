"""
Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its
neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are
connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

Note
Sort the element in the set in increasing order
"""
__author__ = 'Daniel'


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def connectedSet(self, nodes):
        """
        Connected component rather than clique

        :param nodes: {UndirectedGraphNode[]} nodes a array of undirected graph node
        :return: {int[][]} a connected set of a undirected graph
        """
        rets = []
        visisted = set()
        for node in nodes:
            if node not in visisted:
                ret = []
                self.dfs(node, visisted, ret)
                ret.sort()
                rets.append(ret)

        return rets

    def dfs(self, node, visited, ret):
        # pre-call check
        ret.append(node.label)
        visited.add(node)
        for nei in node.neighbors:
            if nei not in visited:
                self.dfs(nei, visited, ret)
