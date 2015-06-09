"""
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example
For push(1), pop(), push(2), push(3), top(), pop(), you should return 1, 2 and 2

Challenge
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.
"""
__author__ = 'Danyang'


class Queue:
    def __init__(self):
        """
        Dual stack
        """
        self.in_stk = []
        self.out_stk = []

    def push(self, element):
        self.in_stk.append(element)

    def top(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        return self.out_stk[-1]

    def pop(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        return self.out_stk.pop()

