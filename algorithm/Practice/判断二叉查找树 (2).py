# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Checker:
    def checkBST(self, root):
        # write code here
        tmp = []
        tmp_res = []
        current = root
        while tmp or current:
            while current:
                tmp.append(current)
                current = current.left
            if tmp:
                now_me = tmp.pop()
                tmp_res.append(now_me)
                current = now_me.right
        for i in range(len(tmp_res)-1):
            if tmp_res[i].val > tmp_res[i+1].val:
                return False
        return True

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        for i in range(len(sequence)-1):
            if sequence[i] < sequence[i+1]:
                return False
        return True