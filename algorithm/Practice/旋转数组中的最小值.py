# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        # while right>left and left>0:
        while True:
            if left == right-1:
                return min(rotateArray[left],rotateArray[right])
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]
            mid = int((right+left)/2)
            if rotateArray[left] > rotateArray[mid]:
                right = mid
                continue
            if rotateArray[mid] > rotateArray[right]:
                left = mid
                continue
            break
        return min(rotateArray)

if __name__ == '__main__':
    Test = Solution()
    arry = [4,5,6,1,2,3]
    print(Test.minNumberInRotateArray(arry))
