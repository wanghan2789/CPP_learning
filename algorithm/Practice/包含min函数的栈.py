# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.helpmin = []

    def push(self, node):
        if not self.stack:
            self.stack.append(node)
            self.helpmin.append(node)
        self.stack.append(node)
        tmp = self.helpmin[-1]
        self.helpmin.append(min(node,tmp))

    def pop(self):
        if not self.stack:
            return
        # write code here
        self.helpmin.pop()
        return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return

    def min(self):
        # write code here
        return self.helpmin[-1]