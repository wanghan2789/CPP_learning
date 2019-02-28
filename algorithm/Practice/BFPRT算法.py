from random import randint


class Solution(object):
    def bfprt(self, arr_list, k):
        num = self.bfprt_fun(arr_list)
        left = 0
        right = len(arr_list) - 1
        num = arr_list[randint(0, right)]
        while True:
            (left, right, arr_list) = self.partition(arr_list, num)
            if k >= left and k <= right:
                return arr_list[k], arr_list
            if k < left:
                num = arr_list[randint(0, left)]
            if k > right:
                num = arr_list[randint(right + 1, len(arr_list) - 1)]

    def bfprt_fun(self, arr_list):
        if len(arr_list) <= 1:
            return arr_list[0]
        if len(arr_list) <= 5:
            arr_list = sorted(arr_list)
            return arr_list[len(arr_list)//2 - 1] if len(arr_list)%2==0 else arr_list[len(arr_list)//2]
        res = []
        start = 0
        while True:
            if start+5 >= len(arr_list):
                res.append(self.bfprt_fun(arr_list[start:]))
                break
            res.append(self.bfprt_fun(arr_list[start:start+5]))
            start += 5
        return self.bfprt_fun(res)

    def sort_theory(self, arr_list, k):
        left = 0
        right = len(arr_list) - 1
        num = arr_list[randint(0,right)]
        while True:
            (left,right,arr_list) = self.partition(arr_list,num)
            if k >= left and k <= right:
                return arr_list[k],arr_list
            if k < left:
                num = arr_list[randint(0, left)]
            if k > right:
                num = arr_list[randint(right+1, len(arr_list)-1)]

    def partition(self, arr_list, num):
        left = -1
        right = len(arr_list)
        current = 0
        while current < right:
            if arr_list[current] < num:
                arr_list[current],arr_list[left+1] = arr_list[left+1],arr_list[current]
                current += 1
                left += 1
            elif arr_list[current] > num:
                arr_list[current], arr_list[right - 1] = arr_list[right - 1], arr_list[current]
                right -= 1
            else:
                current += 1
        zone_left = left+1
        zone_right = right-1
        if right - left == 1 or right == 0 or left == len(arr_list) - 1:
            zone_left,zone_right = -1,-1
        return zone_left, zone_right, arr_list


if __name__ == '__main__':
    Test = Solution()
    # arr = [1,4,5,6,8,4,6,8,5,2,1,4,9]
    # print(Test.sort_theory(arr,9))
    # print(Test.bfprt_fun(arr))
    arr = [1,5,4,6,8,9,2,5,4,3]
    print(sorted(arr))
    print(Test.bfprt_fun(arr))
    print(Test.bfprt(arr,3))
