# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.IsBanlaced = True

    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        self.IsBalancedSolutionFunction(pRoot,1,self.IsBanlaced)
        return self.IsBanlaced

    def IsBalancedSolutionFunction(self,head,level,IsBalance):
        if not head:
            return level
        if self.IsBanlaced:
            left = self.IsBalancedSolutionFunction(head.left,level+1,self.IsBanlaced)
            right = self.IsBalancedSolutionFunction(head.right, level + 1,self.IsBanlaced)
            if abs(left-right)>1:
                self.IsBanlaced = False
                IsBalance = False
                return 0
        return max(right,left)
