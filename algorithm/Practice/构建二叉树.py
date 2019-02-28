class Node(object):
    def __init__(self, value=-1,lchild=None,rchild=None):
        self.data = value
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    # construction
    def __init__(self, root=None):
        self.root = root

    def add(self, elemnt=None):
        if elemnt is not None:
            node = Node(elemnt)
        else:
            node = None
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            # 这是一个巧妙地遍历方法，可以注意到，借助队列进行层序遍历
            while temp:
                current = temp.pop(0)
                if current.lchild is None:
                    current.lchild = node
                    return
                elif current.rchild is None:
                    current.rchild = node
                    return
                else:
                    temp.append(current.lchild)
                    temp.append(current.rchild)

    def printsecondbinarytree(self):
        #直观的打印二叉树
        head = self.root
        self.printfunction(head,0,'H',17)

    def printfunction(self, head, heigh, stringchar, lengh):
        if head is None:
            return
        self.printfunction(head.rchild,heigh+1,'v',lengh)
        pr_str_val = stringchar + str(head.data) + stringchar
        lenSum = len(pr_str_val)
        lenL = int(lenSum/2)
        lenR = lenSum - lenL
        pr_str_val = ' '*lenL + pr_str_val + ' '*lenR
        print(heigh*lengh*' '+ pr_str_val)
        self.printfunction(head.lchild, heigh + 1, '^', lengh)

    def InOrderAfter(self):
        #前序遍历 中左右  递归版本
        head = self.root
        self.InOrderAfterFunction(head)
        print()

    def InOrderAfterFunction(self,head):
        if head is None:
            return
        # print(head.data, end='') #前序遍历
        self.InOrderAfterFunction(head.lchild)
        print(head.data, end='')  #中序遍历
        self.InOrderAfterFunction(head.rchild)
        #print(head.data, end='')  #后序遍历

    def LoopTral(self):
        #非递归版本的遍历
        head = self.root
        self.InOrderAfterNoR(head)
        print()
        self.Level(head)
        print()
        self.LeftRightRoot(head)
        print()

    def InOrderAfterNoR(self, head):
        if head is None:
            return
        tmp = [head]
        while tmp:
            current = tmp.pop()
            if current is not None:
                print(current.data, end=' ')
                if current.rchild is not None:
                    tmp.append(current.rchild)
                if current.lchild is not None:
                    tmp.append(current.lchild)

    def Level(self, head):
        if head is None:
            return
        tmp = [head]
        while tmp:
            current = tmp.pop(0)
            if current is not None:
                print(current.data, end=' ')
                if current.lchild is not None:
                    tmp.append(current.lchild)
                if current.rchild is not None:
                    tmp.append(current.rchild)

    def LeftRightRoot(self,head):
        if head is None:
            return
        tmp = [head]
        another = []
        while tmp:
            current = tmp.pop()
            if current is not None:
                another.append(current)
                if current.lchild is not None:
                    tmp.append(current.lchild)
                if current.rchild is not None:
                    tmp.append(current.rchild)
        while another:
            print(another.pop().data,end=' ')

    def LevelPrint(self):
        head = self.root
        if head is None:
            return
        level = 1
        tmp = [head]
        current_level = head
        after_level = None
        print(level,':',end='')
        while tmp:
            current = tmp.pop(0)
            if current is not None:
                print(current.data,' ',end='')
                if current.lchild is not None:
                    tmp.append(current.lchild)
                    after_level = current.lchild
                if current.rchild is not None:
                    tmp.append(current.rchild)
                    after_level = current.rchild
            if current == current_level and tmp !=[]:
                current_level = after_level
                level += 1
                print()
                print(level,':',end='')
        print()

    def NewCoadP(self):
        head = self.root
        if head is None:
            return
        level = 1
        tmp = [head]
        current_level = head
        after_level = None
        res = [[]]
        while tmp:
            current = tmp.pop(0)
            if current is not None:
                res[-1].append(current.data)
                if current.lchild is not None:
                    tmp.append(current.lchild)
                    after_level = current.lchild
                if current.rchild is not None:
                    tmp.append(current.rchild)
                    after_level = current.rchild
            if current == current_level and tmp != []:
                current_level = after_level
                level += 1
                res.append([])
                # print()
                # print(level, ':', end='')

        print(res)
        # return res

    def Sequence(self):
        head = self.root
        res = ''
        tmp = [head]
        while tmp:
            current = tmp.pop(0)
            if current is not None:
                res += str(current.data)
                res += '!'
                tmp.append(current.lchild)
                tmp.append(current.rchild)
            else:
                res += '#!'
        print(res)
        return res

    def resequence(self,res):
        res = res.split('!')
        root = Node(int(res.pop(0)))
        help = [root]
        while res and help:
            if res[0] == '':
                break
            current = help.pop(0)
            if res[0] != '#':
                current.lchild = Node(int(res.pop(0)))
                help.append(current.lchild)
            else:
                current.lchild = None
                res.pop(0)
            if res[0] == '':
                break
            if res[0] != '#':
                current.rchild = Node(int(res.pop(0)))
                help.append(current.rchild)
            else:
                current.rchild = None
                res.pop(0)
        return root


if __name__ == '__main__':
    # BinaryTree = Tree(Node(1))
    # BinaryTree.add(2)
    # BinaryTree.add(3)
    # BinaryTree.add(4)
    # BinaryTree.add(7)
    # BinaryTree.add(5)
    # BinaryTree.add(6)
    BinaryTree = Tree(Node(7))
    BinaryTree.add(6)
    BinaryTree.add(-1)
    BinaryTree.add(4)
    BinaryTree.add(-1)
    BinaryTree.add(-1)
    BinaryTree.add(-1)
    BinaryTree.add(2)
    BinaryTree.add(5)

    # for i in range(2,10):
    #     BinaryTree.add(i)
    # BinaryTree.printsecondbinarytree()
    # BinaryTree.InOrderAfter()
    # BinaryTree.LoopTral()
    # BinaryTree.LevelPrint()
    # BinaryTree.NewCoadP()
    # res = BinaryTree.Sequence()
    # # res = '1!#!2!3!4!5!6!7!8!9!#!#!#!#!#!#!#!#!#!#!'
    # BinaryTree.root = BinaryTree.resequence(res)
    BinaryTree.printsecondbinarytree()
    BinaryTree.InOrderAfterNoR(BinaryTree.root)
    # BinaryTree.LeftRightRoot(BinaryTree.root)



