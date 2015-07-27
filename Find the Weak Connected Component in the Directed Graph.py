"""
Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of
its neighbors. (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct edge
path.)

Have you met this question in a real interview? Yes
Example
Given graph:

A----->B  C
 \     |  |
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}

Note
Sort the element in the set in increasing order
"""


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return repr(self.x)

from collections import defaultdict
__author__ = 'Daniel'


class UnionFind(object):
    """
    Weighted Union Find with path compression
    """
    def __init__(self):
        self.pi = {}  # item -> Node
        self.sz = {}

    def add(self, item):
        if item not in self.pi:
            self.pi[item] = item
            self.sz[item] = 1

    def union(self, a, b):
        self.add(a)
        self.add(b)

        pi1 = self._pi(a)
        pi2 = self._pi(b)

        if self.sz[pi1] > self.sz[pi2]:
            pi1, pi2 = pi2, pi1

        self.pi[pi1] = pi2
        self.sz[pi2] += self.sz[pi1]

    def _pi(self, item):
        pi = self.pi[item]
        if item != pi:
            self.pi[item] = self._pi(pi)

        return self.pi[item]

    def compress(self):
        for item in self.pi.keys():
            self.pi[item] = self._pi(item)


class Solution:
    def connectedSet2(self, nodes):
        """
        Union-find

        :param nodes: {DirectedGraphNode[]} nodes a array of directed graph node
        :return: {int[][]} a connected set of a directed graph
        """
        uf = UnionFind()
        for node in nodes:
            uf.add(node.label)
            for nei in node.neighbors:
                uf.union(node.label, nei.label)

        uf.compress()
        ret = defaultdict(list)
        for item, pi in uf.pi.items():
            ret[pi].append(item)

        for v in ret.values():
            v.sort()

        return ret.values()

if __name__ == "__main__":
    items = {i: DirectedGraphNode(i) for i in "ABCDEF"}
    items["A"].neighbors.append(items["B"])
    items["A"].neighbors.append(items["D"])
    items["B"].neighbors.append(items["D"])
    items["C"].neighbors.append(items["E"])
    items["F"].neighbors.append(items["E"])
    assert Solution().connectedSet2(items.values()) == [['A', 'B', 'D'], ['C', 'E', 'F']]

