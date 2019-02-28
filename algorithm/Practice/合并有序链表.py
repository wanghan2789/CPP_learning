#OJ
#https://www.nowcoder.com/practice/
# d8b6b4358f774294a89de2a6ac4d9337?
# tpId=13&tqId=11169&tPage=1&rp=1&ru=
# /ta/coding-interviews&qru=/ta/
# coding-interviews/question-ranking
#O(N) O(1)
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
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None and pHead2 is None:
            return None
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        #merg的思想
        res_head = None
        res_current = None
        current1 = pHead1
        current2 = pHead2
        while True:
            if current1 is None or current2 is None:
                if current1 is None and current2 is None:
                    res_current.next = None
                if current1 is None:
                    res_current.next = current2
                if current2 is None:
                    res_current.next = current1
                break
            if current1.val<=current2.val:
                if res_head is None:
                    res_head = current1
                    res_current = res_head
                    current1 = current1.next
                    continue
                else:
                    tmp = current1.next
                    res_current.next = current1
                    res_current = res_current.next
                    current1 = tmp
            else:
                if res_head is None:
                    res_head = current2
                    res_current = res_head
                    current2 = current2.next
                    continue
                else:
                    tmp = current2.next
                    res_current.next = current2
                    res_current = res_current.next
                    current2 = tmp
        return res_head


if __name__ == '__main__':
    A = LinkList()
    A.insert(ListNode(0))
    A.insert(ListNode(1))
    A.insert(ListNode(2))
    B = LinkList()
    B.insert(ListNode(0))
    B.insert(ListNode(1))
    B.insert(ListNode(2))
    A.print_f()
    B.print_f()
    A.head = Solution().Merge(A.head,B.head)
    A.print_f()

