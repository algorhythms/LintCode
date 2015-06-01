"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Have you met this question in a real interview? Yes
Example
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
__author__ = 'Daniel'


class Solution:
    def evalRPN(self, tokens):
        """
        Evaluate postfix. Negative numbers possible

        :param tokens: The Reverse Polish Notation
        :return: the value
        """
        return self.eval_postfix(tokens)

    def eval_postfix(self, post):
        stk = []
        for elt in post:
            if elt.strip("-").isdigit():
                stk.append(int(elt))
            else:
                b = stk.pop()
                a = stk.pop()
                if elt == "+":
                    stk.append(a+b)
                elif elt == "-":
                    stk.append(a-b)
                elif elt == "*":
                    stk.append(a*b)
                else:
                    stk.append(self.__div(a, b))  # 6/-132 should be evaluated to 0 as C-like

        if stk:
            return stk[-1]
        return 0


    def __div(self, a, b):
        sign = 1
        if a*b < 0:
            sign = -1

        return abs(a)/abs(b)*sign