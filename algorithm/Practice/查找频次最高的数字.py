# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        l = len(numbers)
        num = l // 2
        res = 0
        resd = {}
        for i in range(l):
            if numbers[i] not in resd:
                resd[numbers[i]] = 1
            else:
                resd[numbers[i]] += 1
        for i in resd:
            if resd[i] > num:
                return i
        return res


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    Test = Solution()
    print(Test.MoreThanHalfNum_Solution(arr))

