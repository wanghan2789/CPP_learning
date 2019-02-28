import random


# top K
class Solution(object):
    def partition(self, arr, k):
        l = len(arr)
        if not l:
            return
        index = random.randint(0, l)
        num = arr[index]

        pass

    def partition_function(self, arr, left, right, now_num):
        if right < left:
            return []

        current_l = left - 1
        current_r = right + 1
        l_now = left
        while l_now < current_r:
            if arr[l_now] < now_num:
                current_l += 1
                arr[l_now], arr[current_l] = arr[current_l], arr[l_now]
                l_now += 1
            elif arr[l_now] > now_num:
                current_r -= 1
                arr[l_now], arr[current_r] = arr[current_r], arr[l_now]
            else:
                l_now += 1
        return arr


if __name__ == '__main__':
    Test = Solution()
    a = [0,1,5,8,7,6,3,1,2]
    print(Test.partition_function(a,0,len(a),6))