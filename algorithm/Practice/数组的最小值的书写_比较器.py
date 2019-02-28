# -*- coding:utf-8 -*-
# a = [[1,2],[2,1],[1,1],[2,2]]
# print(a)
# a.sort(key=lambda x:(-x[0],x[1]))
# print(a)
from functools import cmp_to_key


class Solution(object):
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return
        a = sorted(numbers,key=cmp_to_key(self.our_cmp))
        res = ''
        for i in range(len(a)):
            res += str(a[i])
        # print(res)
        return int(res)

    def our_cmp(self, x, y):
        if str(x) + str(y) >= str(y) + str(x):
            return 1
        else:
            return -1


if __name__ == '__main__':
    Test = Solution()
    a = [3, 32, 321]
    print(Test.PrintMinNumber(a))