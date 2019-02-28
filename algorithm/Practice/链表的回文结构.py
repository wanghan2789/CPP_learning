#OJ https://www.nowcoder.com/questionTerminal/d281619e4b3e4a60a2cc66ea32855bfa
# -*- coding:utf-8 -*-


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


class PalindromeList:
    def chkPalindrome(self, A):
        # write code here
        if A is None:
            return False
        if A.next is None:
            return True
        head = A
        quick = A
        slow = A
        while True:
            quick = quick.next.next
            if quick is None:
                break
            if quick.next is None:
                slow = slow.next
                break
            slow = slow.next
        mid = slow
        start = mid.next
        current = start
        tmp = current.next
        while tmp is not None:
            after = tmp.next
            tmp.next = current
            current = tmp
            tmp = after
        bool_res = (current.val == head.val)
        tmp = current.next
        while current!= start:
            bool_res = (current.val == head.val and bool_res)
            head = head.next
            after = tmp.next
            tmp.next = current
            current = tmp
            tmp = after
        return bool_res


if __name__ == '__main__':
    A = LinkList()
    A.insert(ListNode(0))
    A.insert(ListNode(1))
    A.insert(ListNode(1))
    A.insert(ListNode(0))
    # A.insert(ListNode(4))
    # A.insert(ListNode(5))
    A.print_f()
    solve = PalindromeList()
    print(solve.chkPalindrome(A.head))






