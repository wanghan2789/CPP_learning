#OJ https://www.nowcoder.com/practice/
# f836b2c43afc4b35ad6adc41ec941dba?tpId=
# 13&tqId=11178&tPage=2&rp=2&ru=/ta/coding-interviews&qru=
# /ta/coding-interviews/question-ranking
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        current = pHead
        #链表的复制 1-2... -> 1-1o-2-2o...
        while current is not None:
            tmp = current.next
            current.next = RandomListNode(current.label)
            current.next.next = tmp
            current = tmp
        #复杂链表的链接
        current = pHead
        while current is not None:
            if current.random is not None:
                current.next.random = current.random.next
            current = current.next.next
        current = pHead
        res_head = current.next
        #链表的分解
        while current is not None:
            tmp = current.next
            current_tmp = current.next.next
            current.next = current_tmp
            if current_tmp is not None:
                tmp.next = current_tmp.next
            else:
                tmp.next = None
            current = current_tmp

        return res_head