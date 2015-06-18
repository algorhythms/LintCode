"""
The structure of Expression Tree is a binary tree to evaluate certain expressions. All leaves of the Expression Tree
have an number string value. All non-leaves of the Expression Tree have an operator string value.

Now, given an expression array, build the expression tree of this expression, return the root of this expression tree.

Example
For the expression (2*6-(23+7)/(1+2)) (which can be represented by ["2" "*" "6" "-" "(" "23" "+" "7" ")" "/" "(" "1" "+"
"2" ")"]). The expression tree will be like

                 [ - ]
             /          \
        [ * ]              [ / ]
      /     \           /         \
    [ 2 ]  [ 6 ]      [ + ]        [ + ]
                     /    \       /      \
                   [ 23 ][ 7 ] [ 1 ]   [ 2 ] .
After building the tree, you just need to return root node [-].
"""
__author__ = 'Daniel'


class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None


class Solution:
    def build(self, expression):
        """

        :param expression: A string list
        :return: The root of expression tree
        """
        post = self.infix2postfix(expression)
        tree_node = self.postfix2tree(post)
        return tree_node

    def infix2postfix(self, expression):
        """

        :param expression:
        :return:
        """
        post = []
        op_stk = []
        for elt in expression:
            if elt.isdigit():
                post.append(elt)
            elif elt == "(":
                op_stk.append(elt)
            elif elt == ")":
                while op_stk and op_stk[-1] != "(":
                    post.append(op_stk.pop())
                op_stk.pop()
            else:
                while op_stk and self.precedence(op_stk[-1]) >= self.precedence(
                        elt):  # notice equal for the order of operators of same precedence.
                    post.append(op_stk.pop())
                op_stk.append(elt)

        while op_stk:
            post.append(op_stk.pop())

        return post

    def postfix2tree(self, post):
        tree_stk = []
        for elt in post:
            if elt.isdigit():
                tree_stk.append(ExpressionTreeNode(elt))
            else:
                pi = ExpressionTreeNode(elt)
                pi.right = tree_stk.pop()
                pi.left = tree_stk.pop()
                tree_stk.append(pi)

        try:
            return tree_stk.pop()
        except IndexError:
            return None

    def precedence(self, elt):
        if elt in ("(", ")"):
            return 0
        if elt in ("+", "-"):
            return 1
        if elt in ("*", "/"):
            return 2
        return 3


if __name__ == "__main__":
    tree_ndoe = Solution().build(["2", "*", "6", "-", "(", "23", "+", "7", ")", "/", "(", "1", "+", "2", ")"])
    assert tree_ndoe.symbol == "-"