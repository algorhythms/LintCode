"""
Given an expression string array, return the Polish notation of this expression. (remove the parentheses)

Example
For the expression [(5 -6) * 7] (which is represented by ["(", "5", "-", "6", ")", "*", "7"]), the corresponding polish
notation is [* - 5 6 7] (which the return value should be ["*", "-", "5", "6", "7"]).
"""
__author__ = 'Daniel'


class Solution:
    def convertToPN(self, expression):
        """
        https://github.com/kamyu104/LintCode/blob/master/C%2B%2B/convert-expression-to-polish-notation.cpp
        need to reverse

        :param expression: A string list
        :return: The Polish notation of this expression
        """
        return self.infix2prefix(expression)

    def infix2prefix(self, lst):
        """
        starting from right the left
        """
        stk = []
        pre = []
        for elt in reversed(lst):
            if elt.isdigit():
                pre.append(elt)
            elif elt == ")":
                stk.append(elt)
            elif elt == "(":
                while stk and stk[-1] != ")":
                    pre.append(stk.pop())
                stk.pop()
            else:
                while stk and self.precedence(elt) < self.precedence(stk[-1]):  # < rather than <=
                    pre.append(stk.pop())
                stk.append(elt)

        while stk:
            pre.append(stk.pop())

        pre.reverse()
        return pre

    def precedence(self, x):
        if x in ("(", ")"):
            return 0
        if x in ("+", "-"):
            return 1
        if x in ("*", "/"):
            return 2
        return 3


if __name__ == "__main__":
    assert Solution().infix2prefix(["(", "5", "-", "6", ")", "*", "7"]) == ['*', '-', '5', '6', '7']