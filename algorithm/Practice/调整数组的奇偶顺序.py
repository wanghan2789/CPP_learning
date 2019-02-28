# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        if n == 0 or n == 1:
            return array
        zone_s = []
        zone_d = []
        for i in range(n):
            if array[i] % 2 == 0:
                zone_d.append(array[i])
            else:
                zone_s.append(array[i])
        return zone_s+zone_d


if __name__ == '__main__':
    Test = Solution()
    a = [i for i in range(10)]
    print(Test.reOrderArray(a))
