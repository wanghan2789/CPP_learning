# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        head = root
        tmp = [head]
        while tmp:
            current = tmp.pop(0)
            current.left, current.right = current.right,current.left
            if current.left:
                tmp.append(current.left)
            if current.right:
                tmp.append(current.right)
        return head
