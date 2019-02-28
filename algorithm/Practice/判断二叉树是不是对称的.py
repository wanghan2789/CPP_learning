# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    # construction
    def __init__(self, root=None):
        self.root = root
        self.tmp = []
        self.current = 0
        self.l = 0
        self.r = 0

    def add(self, elemnt):
        if elemnt is not None:
            node = TreeNode(elemnt)
        else:
            node = None
        if self.root is None:
            self.root = node
            if not self.root:
                return
            self.tmp = [self.root]
            self.current = self.root
        else:
            # 这是一个巧妙地遍历方法，可以注意到，借助队列进行层序遍历
            current = self.tmp.pop(0)
            while not current:
                current = self.tmp.pop(0)
            if current is not None:
                if self.l == 0:
                    current.left = node
                    self.tmp.append(current.left)
                    self.l = 1
                    self.tmp.insert(0, current)
                    return
                if self.r == 0:
                    current.right = node
                    self.tmp.append(current.right)
                    self.l = 0
            # while temp:
            #     current = temp.pop(0)
            #     if current.left is None:
            #         current.left = node
            #         return
            #     elif current.right is None:
            #         current.right = node
            #         return
            #     else:
            #         temp.append(current.left)
            #         temp.append(current.right)

    def printsecondbinarytree(self):
        #直观的打印二叉树
        head = self.root
        self.printfunction(head,0,'H',17)

    def printfunction(self, head, heigh, stringchar, lengh):
        if head is None:
            return
        self.printfunction(head.right,heigh+1,'v',lengh)
        pr_str_val = stringchar + str(head.val) + stringchar
        lenSum = len(pr_str_val)
        lenL = int(lenSum/2)
        lenR = lenSum - lenL
        pr_str_val = ' '*lenL + pr_str_val + ' '*lenR
        print(heigh*lengh*' '+ pr_str_val)
        self.printfunction(head.left, heigh + 1, '^', lengh)


class Solution:
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


    def isSymmetrical(self, pRoot):
        # write code here
        root = pRoot
        if not root:
            return True
        head = root
        tmp = [head]
        tmpM = [head]
        while tmp:
            current = tmp.pop(0)
            currentM = tmpM.pop(0)
            if not current or not currentM:
                if current!= currentM:
                    return False
                continue
            if current.val != currentM.val:
                return False
            tmp.append(current.left)
            tmp.append(current.right)
            tmpM.append(currentM.right)
            tmpM.append(currentM.left)
        if not tmpM and not tmp:
            return True
        return False

        # head = pRoot
        # pMirror = self.Mirror(head)
        # tmp = [head]
        # tmpM = [pMirror]
        # while tmp and tmpM:
        #     current = tmp.pop(0)
        #     currentM = tmpM.pop(0)
        #     if current is None or currentM is None:
        #         if currentM != current:
        #             return False
        #     else:
        #         if current.val != currentM.val:
        #             return False
        #         if not current.left:
        #             if current.left!=currentM.left:
        #                 return False
        #         if not current.right:
        #             if current.right!=currentM.right:
        #                 return False
        #         if current.left:
        #             tmp.append(current.left)
        #         if current.right:
        #             tmp.append(current.right)
        #         if currentM.left:
        #             tmpM.append(currentM.left)
        #         if currentM.right:
        #             tmpM.append(currentM.right)
        # if not tmpM and not tmp:
        #     return True
        # return False

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


if __name__ == '__main__':
    Test = Tree()
    # Test.add(5)
    # Test.add(3)
    # Test.add(3)
    # Test.add(4)
    # Test.add(None)
    # Test.add(None)
    # Test.add(4)
    # Test.add(2)
    # Test.add(None)
    # Test.add(None)
    # Test.add(2)
    # Test.add(1)
    # Test.add(None)
    # Test.add(None)
    # Test.add(1)
    Test.add(1)
    Test.add(2)
    Test.add(5)
    Test.add(3)
    Test.add(4)
    Test.add(6)
    Test.add(7)
    Test.printsecondbinarytree()
    solve = Solution()
    print(solve.isSymmetrical(Test.root))