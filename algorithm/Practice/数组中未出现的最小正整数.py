#https://www.nowcoder.com/courses/6/6/3
# -*- coding:utf-8 -*-
class ArrayMex:
    def findArrayMex(self, A, n):
        # write code here
        #A是数值，n是数组长度
        if n == 0:
            return 0
        l = 0
        r = n
        while l < r:
            if A[l] == l + 1:
                l += 1
            elif A[l] <= l or A[l] > r or A[l] == A[A[l]-1]:
                A[l] = A[r-1]
                r = r - 1
            else:
                #注意下表变换的坑
                tmp = A[l]
                A[l] = A[A[l]-1]
                A[tmp - 1] = tmp
                #A[A[l] - 1] = tmp 错误写法
                #A[tmp-1] = tmp
                #(A[l],A[A[l]-1]) = (A[A[l]-1],A[l])
        return l+1

if __name__ == '__main__':
    Test = ArrayMex()
    # Test.A = [-1,2,3,4]
    # Test.n = 4
    A = [i for i in range(7)]
    A[6] = 0
    print(Test.findArrayMex(A,7))