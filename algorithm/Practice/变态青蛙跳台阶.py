# -*- coding:utf-8 -*-
#newcoad
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==0 or number==1:
            return 1
        else:
            return 2*self.jumpFloorII(number-1)