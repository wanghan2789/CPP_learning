#                   _oo8oo_
#                  o8888888o
#                  88" . "88
#                  (| -_- |)
#                  0\  =  /0
#                ___/'==='\___
#              .' \\|     |// '.
#             / \\|||  :  |||// \
#            / _||||| -:- |||||_ \
#           |   | \\\  -  /// |   |
#           | \_|  ''\---/''  |_/ |
#           \  .-\__  '-'  __/-.  /
#         ___'. .'  /--.--\  '. .'___
#      ."" '<  '.___\_<|>_/___.'  >' "".
#     | | :  `- \`.:`\ _ /`:.`/ -`  : | |
#     \  \ `-.   \_ __\ /__ _/   .-` /  /
# =====`-.____`.___ \_____/ ___.`____.-`=====
#                   `=---=`
#           佛祖保佑         永无bug
#            新年おめでとうございます
# coding=utf-8
# -*- coding: UTF-8 -*-
# 适用于Python3


class TreeNode:
    def __init__(self, value = None, lchild = None, rchild = None, parent = None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.parent = parent

    def is_leaf(self):
        return not self.lchild and not self.rchild

    def is_rchild(self):
        if not self.parent:
            return None
        return self.parent.rchild == self


class BaseSearchTreeClass:
    def __init__(self, value = None):
        if not value:
            self.head = None
        else:
            self.head = TreeNode(value)
        # Tree size
        self.size = 1 if self.head else 0

    def print_in_order(self, head):
        if not head:
            return
        self.PrintInOrder(head.lchild)
        print(head.value)
        self.PrintInOrder(head.rchild)

    def print_pre_order(self, head):
        if not head:
            return
        print(head.value)
        self.print_pre_order(head.lchild)
        self.print_pre_order(head.rchild)

    def print_post_order(self, head):
        if not head:
            return
        self.print_post_order(head.lchild)
        self.print_post_order(head.rchild)
        print(head.value)

    @staticmethod
    def get_min_node(head):
        tmp = head
        while tmp.lchild:
            tmp = tmp.lchild
        return tmp

    @staticmethod
    def get_max_node(head):
        tmp = head
        while tmp.rchild:
            tmp = tmp.rchild
        return tmp

    def look_construction_of_tree(self, head):
        if not head:
            return
        tmp = head
        self.deal_tree_sequence(tmp)

    def deal_tree_sequence(self, head):
        if head.rchild:
            self.deal_tree_branch(head.rchild, True, '')
        self.print_node_value(head)
        if head.lchild:
            self.deal_tree_branch(head.lchild, False, '')

    def deal_tree_branch(self, head, is_right_tree, indent):
        if head.rchild:
            self.deal_tree_branch(head.rchild, True, indent+("        " if is_right_tree else " |      "))
        print(indent, end='')
        if is_right_tree:
            print(" /", end='')
        else:
            print(" \\", end='')
        print("----- ", end='')
        self.print_node_value(head)
        if head.lchild:
            self.deal_tree_branch(head.lchild, False, indent + ("        " if is_right_tree else " |      "))

    @staticmethod
    def print_node_value(head):
        if not head:
            print("None")
        else:
            print(head.value)

    def get_size(self):
        return self.size

    def search_element(self, element):
        tmp = self.head
        while tmp and tmp.value != element:
            if element < tmp.value:
                tmp = tmp.lchild
            else:
                tmp = tmp.rchild
        return tmp

    # 对一般的搜索树，我需要后继节点
    @staticmethod
    def search_descendant_node(head):
        tmp = head
        if not tmp:
            return
        if tmp.rchild:
            res = tmp.rchild
            while res.lchild:
                res = res.lchild
            return res
        else:
            current = tmp
            parent = tmp.parent
            while parent and current == parent.rchild:
                current = parent
                parent = current.parent
            return parent

    def insert_element(self, element):
        tmp = self.head
        if not tmp:
            self.head = TreeNode(element)
            return
        while tmp and tmp.value != element:
            if element < tmp.value:
                if not tmp.lchild:
                    tmp.lchild = TreeNode(element, None, None, tmp)
                    self.size += 1
                    return
                else:
                    tmp = tmp.lchild
            else:
                if not tmp.rchild:
                    tmp.rchild = TreeNode(element, None, None, tmp)
                    self.size += 1
                    return
                else:
                    tmp = tmp.rchild

    def delete_element(self, element):
        deal_ele_node = self.search_element(element)
        if not deal_ele_node:
            return
        if deal_ele_node.is_leaf():
            self.transplant(deal_ele_node, None)
            self.size -= 1
            return
        if not deal_ele_node.lchild:
            self.transplant(deal_ele_node, deal_ele_node.rchild)
            self.size -= 1
            return
        if not deal_ele_node.rchild:
            self.transplant(deal_ele_node, deal_ele_node.lchild)
            self.size -= 1
            return
        # 这是一个一般节点，get到刚好比当前节点打的节点
        after_node = self.get_min_node(deal_ele_node.rchild)
        if after_node.parent != deal_ele_node:
            self.transplant(after_node, after_node.rchild)
            # 保留删除节点的右子树
            after_node.right = deal_ele_node.rchild
            after_node.right.parent = after_node
        self.transplant(deal_ele_node, after_node)
        after_node.lchild = deal_ele_node.lchild
        after_node.lchild.parent = after_node
        self.size -= 1
        return

    def transplant(self, replace_node, new_node):
        if not replace_node.parent:
            self.head = new_node
        else:
            if replace_node.is_rchild:
                replace_node.parent.rchild = new_node
            else:
                replace_node.parent.lchild = new_node
        if new_node:
            new_node.parent = replace_node.parent

    def test_help(self, test_insert, test_delete, is_purse=False):
        for i in test_insert:
            self.insert_element(i)
            self.look_construction_of_tree(self.head)
            print('--Test Cycle--')
            if is_purse:
                input()
        for i in test_delete:
            self.delete_element(i)
            self.look_construction_of_tree(self.head)
            print('--Test Cycle--')
            if is_purse:
                input()


if __name__ == '__main__':
    TestBase = BaseSearchTreeClass()
    TestBase.test_help([4,2,6,0,3,5,7,7], [3,4])



