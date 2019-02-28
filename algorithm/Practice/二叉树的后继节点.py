# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        if pNode.right is not None:
            current = pNode.right
            while current.left is not None:
                current = current.left
            return current
        # if pNode.next is None or pNode == pNode.next:
        #     return None
        # if pNode == pNode.next.left:
        #     return pNode.next
        # if pNode == pNode.next.right:
        x = pNode
        parent = pNode.next
        while parent is not None:
            if x == parent.left:
                return parent
            else:
                x = x.next
                parent = parent.next
        return None