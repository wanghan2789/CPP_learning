# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#待验证！


class Solution:
    @staticmethod
    def depth_tree(self, root):
        head = root
        level = 1
        while head:
            head = head.left
            level += 1
        return level

    def num_of_tree(self, root):
        if not root:
            return 0
        head = root
        depth = self.depth_tree(root)
        res = self.num_of_tree_function(head, depth, 1)
        return res

    def num_of_tree_function(self, head, depth, level):
        if not head:
            return 0
        current = head
        if not current.right:
            return 2
        level_current = self.depth_tree(head) + 1
        if level_current == depth:
            return 2**(depth-level) + self.num_of_tree_function(current.right,depth,level+1)
        else:
            return 2**(depth-level_current) + self.num_of_tree_function(current.left,depth,level+1)
