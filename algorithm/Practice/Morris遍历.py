class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, head=None):
        self.head = head
        self.tmp = [self.head] if head else []
        self.current = None
        self.flag = 0

    def add(self, node=None):
        if not self.head:
            self.head = node
            self.tmp = [self.head]
            return
        current = self.tmp[0]
        if not self.flag:
            self.flag += 1
            current.left = node
            if node:
                self.tmp.append(current.left)
            return
        current = self.tmp.pop(0)
        self.flag = 0
        current.right = node
        if node:
            self.tmp.append(current.right)
        return

    def level(self):
        current = self.head
        tmp = [current]
        last = current
        nlast = None
        while tmp:
            current = tmp.pop(0)
            print(current.val, end=' ')
            if current.left:
                tmp.append(current.left)
                nlast = current.left
            if current.right:
                tmp.append(current.right)
                nlast = current.right
            if current == last:
                print()
                last = nlast

    def morris(self):
        current = self.head
        while current:
            if not current.left:
                print(current.val,end=' ')
                #current = current.right
            else:
                mostright = current.left
                while mostright.right and mostright.right != current:
                    mostright = mostright.right
                if not mostright.right:
                    mostright.right = current
                    print(current.val, end=' ')
                    current = current.left
                    continue
                else:
                    mostright.right = None
            current = current.right





if __name__ == '__main__':
    binary = Tree(Node(0))
    binary.add(Node(1))
    binary.add(None)
    binary.add(Node(3))
    binary.add(Node(4))
    binary.add(Node(5))
    binary.add(Node(6))
    binary.add(Node(7))
    binary.add(Node(8))
    binary.level()
    print('-'*10)
    binary.morris()




