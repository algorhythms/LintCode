"""
Given an expression string array, return the final result of this expression

Example
For the expression 2*6-(23+7)/(1+2), input is

[
  "2", "*", "6", "-", "(",
  "23", "+", "7", ")", "/",
  (", "1", "+", "2", ")"
],
return 2

Note
The expression contains only integer, +, -, *, /, (, ).
"""
__author__ = 'Daniel'


class Solution:
    def evaluateExpression(self, expression):
        """
        List + Stack

        a individual number has the highest precedence

        postfix is in increasing precedence order
        :param expression: a list of strings;
        :return: an integer
        """
        post = self.infix2postfix(expression)
        return self.eval_postfix(post)

    def infix2postfix(self, lst):
        stk = []
        post = []  # post fix expression with increasing precedence order
        for elt in lst:
            if elt.isdigit():
                post.append(elt)
            else:
                if elt == "(":
                    stk.append(elt)
                elif elt == ")":
                    while stk and stk[-1] != "(":
                        post.append(stk.pop())
                    stk.pop()  # pop "("
                else:
                    while stk and self.precedence(elt) <= self.precedence(stk[-1]):
                        post.append(stk.pop())
                    stk.append(elt)

        while stk:
            post.append(stk.pop())

        return post

    def eval_postfix(self, post):
        stk = []
        for elt in post:
            if elt.isdigit():
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
                    stk.append(a/b)

        if stk:
            return stk[-1]
        return 0

    def precedence(self, a):
        if a in ("(", ")"):
            return 0
        if a in ("+", "-"):
            return 1
        if a in ("*", "/"):
            return 2
        return 3


if __name__ == "__main__":
    t = [
        "2", "*", "6", "-", "(",
        "23", "+", "7", ")", "/",
        "(", "1", "+", "2", ")"
    ]
    assert Solution().evaluateExpression(list("1+5")) == 6
    assert Solution().evaluateExpression(t)==2