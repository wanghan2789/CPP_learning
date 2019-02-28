from random import randint
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self, node= None):
        self.head = node

    def insert(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def print_f(self):
        current = self.head
        while current is not None:
            print(current.val,end=' ')
            current = current.next
        print()

class ArrangList:
    def arrang(self, A, value=0):
        # write code here
        if A is None or A.next is None:
            return A
        head = A
        current = head
        our_dict = {}
        while current is not None:
            if current.val < value:
                if 'less' not in our_dict:
                    our_dict['less'] = current
            if current.val == value:
                if 'equal' not in our_dict:
                    our_dict['equal'] = current
            if current.val > value:
                if 'more' not in our_dict:
                    our_dict['more'] = current
            if 'less' in our_dict and 'equal' in our_dict and 'more' in our_dict:
                break
            current = current.next
        less_head = None
        less = less_head
        equal_head = None
        equal = equal_head
        more_head = None
        more = more_head
        if 'less' in our_dict:
            less_head = our_dict['less']
            less = less_head
        if 'equal' in our_dict:
            equal_head = our_dict['equal']
            equal = equal_head
        if 'more' in our_dict:
            more_head = our_dict['more']
            more = more_head

        current = head
        while current is not None:
            if current.val < value:
                if current == less_head:
                    pass
                else:
                    less.next = current
                    less = current
            if current.val == value:
                if current == equal_head:
                    pass
                else:
                    equal.next = current
                    equal = current
            if current.val > value:
                if current == more_head:
                    pass
                else:
                    more.next = current
                    more = current
            current = current.next
        if less is not None:
            less.next = None
        if equal is not None:
            equal.next = None
        if more is not None:
            more.next = None

        res_head = None
        if less_head is not None:
            res_head = less_head
            less.next = equal_head
        if res_head is None:
            res_head = equal_head
            if res_head is not None:
                if equal_head is not None:
                    equal.next = more_head
        else:
            equal.next = more_head
        if res_head is None:
            res_head = more_head
        return res_head


if __name__ == '__main__':
    A = LinkList()
    for i in range(10):
        A.insert(ListNode(randint(0,10)))
    A.print_f()
    solve = ArrangList()
    A.head = solve.arrang(A.head,5)
    A.print_f()






