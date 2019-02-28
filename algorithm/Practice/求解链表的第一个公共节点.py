# -*- coding:utf-8 -*-
#OJ NewCoad
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        loop1 = self.EntryNodeOfLoop(pHead1)
        loop2 = self.EntryNodeOfLoop(pHead2)
        if loop1 is None and loop2 is not None:
            return None
        if loop2 is None and loop1 is not None:
            return None
        if loop1 is not None and loop2 is not None and loop1!=loop2:
            current = loop1.next
            while True:
                if current == loop2:
                    return loop1
                if current == loop1:
                    return None
                current = current.next
        end = None
        if loop1 is not None and loop2 is not None:
            end = loop1
            l1 = self.mylen(pHead1,end)
            l2 = self.mylen(pHead2,end)
        if loop1 is None and loop2 is None:
            (l1,endNode1) = self.mylen(pHead1, end)
            (l2,endNode2) = self.mylen(pHead2, end)
            if endNode1 != endNode2:
                return None
        (current_quick,current_slow) = (pHead1,pHead2) if l1>=l2 else (pHead2,pHead1)
        for i in range(abs(l1-l2)):
            current_quick = current_quick.next
        while current_quick is not None:
            if current_quick == current_slow:
                return current_quick
            current_slow = current_slow.next
            current_quick = current_quick.next

    def mylen(self,pHead,end=None):
        p = pHead
        res = 0
        endNode = None
        while p != end:
            res += 1
            if p.next is None:
                endNode = p
            p = p.next
        if end is not None:
            return res
        else:
            return (res,endNode)

    #本函数用于查找loop的入口
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        current_quick = pHead
        current_slow = pHead
        while True:
            try:
                current_slow = current_slow.next
                current_quick = current_quick.next.next
            except:
                return None
            if current_quick is None or current_slow is None:
                return None
            if current_quick == current_slow:
                current_quick = pHead
                break
        while True:
            if current_quick == current_slow:
                return current_quick
            current_quick = current_quick.next
            current_slow = current_slow.next