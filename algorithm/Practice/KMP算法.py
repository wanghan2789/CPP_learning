#kmp算法的实现
import random


class Solution(object):
    def __init__(self, string=''):
        self.nextarr = []
        self.del_str = string

    def match(self, string, match):
        # if match in string
        n = len(string)
        m = len(match)
        if string == match:
            return 0
        if m > n:
            return -1
        match_next_arr = self.get_nextarr_function(match)
        i = 0
        j = 0
        while i < n and j < m:
            if string[i] == match[j]:
                i += 1
                j += 1
            else:
                if match_next_arr[j] == -1:
                    i += 1
                else:
                    j = match_next_arr[j]
        return i - j if j == m else -1

    def get_nextarr_function(self, string=''):
        if not string:
            return []
        n = len(string)
        current = 2 #len(res)
        res = [-1,0]
        i = 1
        c = 0
        if len(string)  == 1:
            return [-1]
        if len(string) == 2:
            return [-1,0]
        else:
            while current < n:
                if string[current-1] == string[c]:
                    c += 1
                    current += 1
                    res.append(c)
                else:
                    if c > 0:
                        c = res[c]
                    else:
                        current += 1
                        res.append(0)
        return res

    def arr_match(self,m=1000):
        for i in range(m):
            string = ''
            for i in range(random.randint(0,100)):
                string += str(random.randint(0,10))
            if self.get_nextarr_function() != self.arr_match_function():
                print('Fuck')
                print(string)
                return 'Fuck'
        print('ok')
        return 'ok'

    def arr_match_function(self, string):
        n = len(string)
        if not n:
            return []
        if n == 1:
            return [-1]
        if n == 2:
            return [-1, 0]
        res = [-1, 0]


if __name__ == '__main__':
    Test = Solution()
    # print(Test.get_nextarr_function('abc1abc1'))
    print(Test.match('abcac','ac'))