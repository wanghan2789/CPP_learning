class Solution(object):
    def __init__(self, string=''):
        self.string = string

    def manacher(self, string=""):
        string = self.pre_del(string)
        arr_help = []  #记录最长回文半径
        pr = -1  #记录到达的最右边界数值
        index = 0  #最近一次更新的时候回文center
        for i in range(len(string)):
            if not i:
                arr_help.append(1)
                pr = 0
                index = 0
                continue
            if i > pr:
                radius = self.core_del(string, i)
                arr_help.append(radius)
                pr = max(pr, i-1+radius)
                index = i
            else:
                io = i - (i - index) * 2
                il = io - (arr_help[io] - 1)
                lim_left = pr - (pr - index) * 2
                if il < lim_left:
                    arr_help.append(arr_help[io])
                    continue
                if il > lim_left:
                    arr_help.append(pr - i + 1)
                    continue
                if il == lim_left:
                    radius = self.core_del(string, i)
                    arr_help.append(radius)
                    if i - 1 + radius > pr:
                        pr = i - 1 + radius
                        index = i
        return max(arr_help) - 1

    def pre_del(self, string=''):
        if not string:
            string = self.string
        res = ''
        for i in range(2*len(string)+1):
            res += '#' if i%2 == 0 else string[(i-1)//2]
        return res

    def core_del(self,string,index):
        left = index
        right = index
        radius = 0
        while left>=0 and right<len(string) and string[left]==string[right]:
            left -= 1
            right += 1
            radius += 1
        return radius


if __name__ == '__main__':
    Test = Solution()
    print(Test.pre_del('123456789'))
    print(Test.core_del('#c#b#c#',3))
    print(Test.manacher('456789987654'))