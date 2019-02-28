# -*- coding:utf-8 -*-
#OJ : newcoad
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
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