# -*- coding:utf-8 -*-
class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self,node):
        if node is None:
            return
        self.stack.append(node)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def isNone(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def initial(self):
        self.stack = []

class Solution:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2_que = Stack()

    def push(self, node):
        if node is None:
            return
        self.stack1.initial()
        while not self.stack2_que.isNone():
            self.stack1.push(self.stack2_que.pop())
        self.stack1.push(node)
        while not self.stack1.isNone():
            self.stack2_que.push(self.stack1.pop())

    def pop(self):
        return self.stack2_que.pop()