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
#       适用于Python3, write by Malfoy


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
            self.deal_tree_branch(head.lchild, False, indent + (" |      " if is_right_tree else "        "))

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
            return self.head
        while tmp and tmp.value != element:
            if element < tmp.value:
                if not tmp.lchild:
                    tmp.lchild = TreeNode(element, None, None, tmp)
                    self.size += 1
                    return tmp.lchild
                else:
                    tmp = tmp.lchild
            else:
                if not tmp.rchild:
                    tmp.rchild = TreeNode(element, None, None, tmp)
                    self.size += 1
                    return tmp.rchild
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
            after_node.rchild = deal_ele_node.rchild
            after_node.rchild.parent = after_node
        self.transplant(deal_ele_node, after_node)
        after_node.lchild = deal_ele_node.lchild
        after_node.lchild.parent = after_node
        self.size -= 1
        return

    def transplant(self, replace_node, new_node):
        if not replace_node.parent:
            self.head = new_node
        else:
            if replace_node.is_rchild():
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


#     将node进行左旋或右旋
# .*. 头指针倒向哪个方向就是如何旋转
# .*. 多出来的部分转移到空的部分
class BaseMethod(BaseSearchTreeClass):
    def left_rotation(self, nodein):
        node = nodein
        if not node:
            return
        xr = node.rchild
        if not xr:
            return
        node_is_rchild = node.is_rchild()
        xrl = xr.lchild
        if xrl:
            xrl.parent = node
        node.rchild = xrl
        xr.parent = node.parent
        xr.lchild = node
        node.parent = xr
        if not xr.parent:
            self.head = xr
        else:
            if node_is_rchild:
                xr.parent.rchild = xr
            else:
                xr.parent.lchild = xr
        return xr

    def right_rotation(self, nodein):
        node = nodein
        if not node:
            return
        xr = node.lchild
        if not xr:
            return
        node_is_rchild = node.is_rchild()
        xrl = xr.rchild
        if xrl:
            xrl.parent = node
        node.lchild = xrl
        xr.parent = node.parent
        xr.rchild = node
        node.parent = xr
        if not xr.parent:
            self.head = xr
        else:
            if node_is_rchild:
                xr.parent.rchild = xr
            else:
                xr.parent.lchild = xr
        return xr

    def test_rotate(self, test_insert, is_purse=False):
        for i in test_insert:
            self.insert_element(i)
            # if is_purse:
            #     input()
        self.look_construction_of_tree(self.head)
        print('--Construction Complete--')
        for i in test_insert:
            tmp = self.search_element(i)
            if is_purse:
                input()
                print('--Now LRotate' + str(i) + '--')
                self.left_rotation(tmp)
                self.look_construction_of_tree(self.head)
        for i in test_insert:
            tmp = self.search_element(i)
            if is_purse:
                input()
                print('--Now RRotate' + str(i) + '--')
                self.right_rotation(tmp)
                self.look_construction_of_tree(self.head)


# 测试区，测试基础的二叉查找树的插入和删除
def test_base():
    TestBase = BaseSearchTreeClass()
    # TestBase.test_help([4,2,6,0,3,5,7,7], [3,4], True)
    TestBase.test_help([4, 2, 6, 0, 3, 5, 7, 7], [3, 4, 5, 7, 7, 0, 2, 6])


# 测试左旋与右旋
def test_rotation():
    Testrotate = BaseMethod()
    Testrotate.test_rotate([4, 2, 6, 0, 3, 5, 7, 7], True)


if __name__ == '__main__':
    Testrotate = BaseMethod()
    Testrotate.test_rotate([4, 2, 6, 0, 3, 5, 7, 7], True)


