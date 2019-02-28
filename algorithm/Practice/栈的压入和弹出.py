# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == popV[::-1]:
            return True

        tmp = []
        i = 0
        ll = len(popV)
        while popV:
            if pushV:
                tmp.append(pushV.pop(0))
            if tmp[-1] == popV[-1]:
                tmp.pop()
                popV.pop()
            i += 1
            if i > 3 * ll:
                return False
        return True

if __name__ == '__main__':
    Test = Solution()
    print(Test.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))
    print(Test.IsPopOrder([1, 2, 3, 4, 5], [4,3,5,1,2]))