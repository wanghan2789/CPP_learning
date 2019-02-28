# 链接：https: // www.nowcoder.com / questionTerminal / 8a19cbe657394eeaac2f6ea9b0f6fcf6
#
#
# / *先序遍历第一个位置肯定是根节点node，
#
# 中序遍历的根节点位置在中间p，在p左边的肯定是node的左子树的中序数组，p右边的肯定是node的右子树的中序数组
#
# 另一方面，先序遍历的第二个位置到p，也是node左子树的先序子数组，剩下p右边的就是node的右子树的先序子数组
#
# 把四个数组找出来，分左右递归调用即可
#
# * /
# 前序遍历第一个是head
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        head = TreeNode(pre[0])
        tin_index = tin.index(pre[0])
        head.left = self.reConstructBinaryTree(pre[1:tin_index+1],tin[0:tin_index])
        head.right = self.reConstructBinaryTree(pre[tin_index+1:],tin[tin_index+1:])
        return head