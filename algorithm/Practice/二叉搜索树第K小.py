# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.falg = False
        self.res = 0
        self.calculate_num = 1
        self.k = 0
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        #二叉搜索树中序遍历的时候是升序的
        if k == 0:
            return None
        self.k = k
        self.InOrderAfterFunction(pRoot)
        if self.falg:
            return self.res
        else:
            return None

    def InOrderAfterFunction(self,head):
        if head is None:
            return
        if not self.falg:
            self.InOrderAfterFunction(head.left)
            #print(head.data, end='')  #中序遍历
            if self.calculate_num == self.k:
                self.falg = True
                self.res = head
                self.calculate_num += 1
                return
            self.calculate_num += 1
            self.InOrderAfterFunction(head.right)



    def InLeftRight(self, root, k, calculate_num):
        if root is None:
            return
        if not self.falg:
            self.InLeftRight(root.left,k,self.calculate_num)
            if calculate_num == k:
                self.falg = True
                self.res = root.val
                return
            self.calculate_num += 1
            self.InLeftRight(root.right,k,self.calculate_num)


