# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []

    def insert(self, elemnt):
        if len(self.arr) == 0:
            self.arr.append(elemnt)
            return
        else:
            self.arr.append(elemnt)
            index = len(self.arr) - 1
            while index > 0:
                if self.arr[int((index-1)/2)] < self.arr[index]:
                    (self.arr[int((index-1)/2)], self.arr[index]) = \
                        (self.arr[index], self.arr[int((index-1)/2)])
                    index = int((index-1)/2)
                else:
                    break

    def modify(self, element):
        if element > self.arr[0]:
            return
        else:
            index = 0
            self.arr[index] = element
            while index < len(self.arr):
                if 2 * index + 1 >= len(self.arr):
                    break
                if 2 * index + 2 >= len(self.arr):
                    if self.arr[index] >= self.arr[2*index+1]:
                        break
                    else:
                        (self.arr[index], self.arr[2 * index + 1]) = (self.arr[2 * index + 1], self.arr[index])
                        index = 2 * index + 1
                        continue
                if self.arr[index] >= self.arr[2*index+1] and self.arr[index] >= self.arr[2*index+1]:
                    break
                if self.arr[2*index+1] > self.arr[2*index+2]:
                    (self.arr[index], self.arr[2*index+1]) = (self.arr[2*index+1], self.arr[index])
                    index = 2*index+1
                    continue
                else:
                    (self.arr[index], self.arr[2 * index + 2]) = (self.arr[2 * index + 2], self.arr[index])
                    index = 2 * index + 2
                    continue

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) <= k:
            return tinput
        for i in range(k):
            self.insert(tinput[i])
        for i in range(k,len(tinput)):
            self.modify(tinput[i])
        return self.arr

    def GetLeastNumbers_SolutionNew(self, tinput, k):
        # write code here
        if len(tinput) <= k:
            tinput.sort()
            return tinput
        tinput.sort()
        return tinput[0:k]


if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    k = 4
    Test = Solution()

    # print(Test.GetLeastNumbers_Solution(a, k))
    print(Test.GetLeastNumbers_SolutionNew(a,k))
