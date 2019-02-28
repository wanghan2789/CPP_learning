# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        for i in range(len(sequence)-1):
            if sequence[i] < sequence[i+1]:
                return False
        return True