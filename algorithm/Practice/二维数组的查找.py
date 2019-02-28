# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        if row == 0:
            return False
        try:
            col = len(array[0])
            if col == 0:
                return False
            if target < array[0][0] or target > array[row-1][col-1]:
                return False
            cur_row = 0
            cur_col = col - 1
            while cur_row < row and cur_col >= 0:
                compare = array[cur_row][cur_col]
                if compare == target:
                    return True
                if compare > target:
                    cur_col -= 1
                if compare < target:
                    cur_row += 1
            return False
        except:
            if target < array[0]:
                return False
            if target > array[row-1]:
                return False
            if target in array:
                return True
            else:
                return False




arr1 = [i for i in range(0,10000)]
arr2 = [i for i in range(1,10001)]
arr3 = [i for i in range(2,10002)]
arr = [arr1,arr2,arr3]
A = Solution()
print(A.Find(100000,arr))
