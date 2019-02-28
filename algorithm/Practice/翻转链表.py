# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def __init__(self, node=None):
        self.node = node

    def insert(self, value):
        node = ListNode(value)
        if self.node is None:
            self.node = node
            return
        current = self.node
        while self.node.next is not None:
            self.node = self.node.next
        self.node.next = node
        self.node = current

    def look(self):
        current = self.node
        while self.node is not None:
            print(self.node.val,end=" ")
            self.node = self.node.next
        self.node = current
        print()

    # 返回ListNode
    def ReverseList(self):
        # write code here
        pHead = self.node
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        current = pHead
        next = pHead.next

        while current is not None:
            if current.next is None:
                current.next = pre
                break
            else:
                current.next = pre
                pre = current
                current = next
                next = current.next
        self.node = current
        return current
# end Test

if __name__ == '__main__':
    test = List()
    test.insert(1)
    test.insert(2)
    test.insert(3)
    test.insert(4)
    test.insert(5)
    test.look()
    test.ReverseList()
    test.look()