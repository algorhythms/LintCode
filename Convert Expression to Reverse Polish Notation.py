"""
Given an expression string array, return the Reverse Polish notation of this expression. (remove the parentheses)

Example
For the expression [3 - 4 + 5] (which denote by ["3", "-", "4", "+", "5"]), return [3 4 - 5 +] (which denote by ["3",
"4", "-", "5", "+"])
"""
__author__ = 'Daniel'


class Solution(object):
    def convertToRPN(self, expression):
        """

        :param expression: A string list
        :return: The Reverse Polish notation of this expression
        """
        return self.infix2postfix(expression)

    def infix2postfix(self, lst):
        """
        The stack temporarily stores the operators of strictly increasing precedence order.

        :param lst:
        :return:
        """
        stk = []
        ret = []  # post fix
        for elt in lst:
            if elt.isdigit():
                ret.append(elt)
            elif elt == "(":
                stk.append(elt)
            elif elt == ")":
                while stk and stk[-1] != "(":
                    ret.append(stk.pop())
                stk.pop()  # pop "("
            else:
                while stk and self.precedence(elt) <= self.precedence(stk[-1]):
                    ret.append(stk.pop())
                stk.append(elt)

        while stk:  # clean up
            ret.append(stk.pop())

        return ret

    def precedence(self, x):
        if x in ("(", ")"):
            return 0
        if x in ("+", "-"):
            return 1
        if x in ("*", "/"):
            return 2
        return 3

if __name__ == "__main__":
    print Solution().infix2postfix(["3", "-", "4", "+", "5"])