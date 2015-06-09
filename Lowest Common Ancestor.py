"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Example
        4

    /     \

  3         7

          /     \

        5         6

For 3 and 5, the LCA is 4.

For 5 and 6, the LCA is 7.

For 6 and 7, the LCA is 7.
"""
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return repr(self.val)


class Solution:
    def lowestCommonAncestor(self, root, A, B):
        """
        O(n) for find path

        ...>LCA***>A
        ...>LCA####>B
        Any node on two paths before LCA are equal respectively
        Any node on two paths after LCA are different respectively

        1. get the paths from root to A and from root to B
        2. cut longer path's tail to make two equal length
        3. scan backward to find the first common ancestor

        :type root: TreeNode
        :type A: TreeNode
        :type B: TreeNode
        :param root: The root of the binary search tree.
        :param A: node in a Binary.
        :param B: node
        :return: Return the least common ancestor(LCA) of the two nodes.
        """
        p1 = self.path(root, A)
        p2 = self.path(root, B)
        p1.append(TreeNode(0))  # dummy
        p2.append(TreeNode(0))  # dummy
        for ind, val in enumerate(p1):
            if val != p2[ind]:
                return p1[ind-1]

    def path(self, root, target):
        """
        path from root to target

        :param target:
        :return:
        """
        ans = []
        self.get_path(root, target, [], ans)
        return ans

    def get_path(self, cur, target, path, ans):
        """

        :param cur:
        :param target:
        :param path:
        :param ans:
        :return: bool
        """
        if not cur:
            return False

        path.append(cur)

        if cur == target:  # compare by reference
            # ans = path
            ans.extend(path)  # otherwise lose reference
            return True

        if cur.left and self.get_path(cur.left, target, path, ans):
            return True

        if cur.right and self.get_path(cur.right, target, path, ans):
            return True

        path.pop()
        return False


if __name__ == "__main__":
    node = TreeNode(1)
    print Solution().lowestCommonAncestor(node, node, node)

    nodes = dict(zip(range(3, 8), [TreeNode(i) for i in range(3, 8)]))
    nodes[4].left = nodes[3]
    nodes[4].right = nodes[7]
    nodes[7].left = nodes[5]
    nodes[7].right = nodes[6]
    print Solution().lowestCommonAncestor(nodes[4], nodes[3], nodes[5])
