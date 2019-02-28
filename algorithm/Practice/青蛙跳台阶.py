import sys
sys.setrecursionlimit(1000000)
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 1:
            return 1
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

A = Solution()
print(A.jumpFloor(100))
