from random import randint

class Test:
    def __init__(self, min, max, num, list = []):
        if list != []:
            self.list = list
            return
        self.list = []
        for i in range(num):
            self.list.append(randint(min, max))

    def look(self):
        print('the list', self.list)

    def max_gaptest(self):
        if len(self.list)< 2:
            return 0
        test = sorted(self.list)
        #print(test)
        # print(self.list)
        testgap = test[1] - test[0]
        for i in range(len(test) - 1):
            if test[i + 1] - test[i] > testgap:
                testgap = test[i + 1] - test[i]
        print("the right", testgap)
        return testgap

    def maxgap(self):
        if len(self.list)< 2:
            return 0
        num_min = min(self.list)
        num_max = max(self.list)
        res = -1
        if num_max == num_min:
            res = 0
        else:
            N = len(self.list)
            dict_min = [-1 for x in range(N + 1)]
            dict_max = [-1 for x in range(N + 1)]
            for i in self.list:
                base = N * (i-num_min)/(num_max-num_min)
                base = int(base)
                # if base not in dict_min:
                #     dict_min[base] = i
                # else:
                #     dict_min[base] = min(i,dict_min[base])
                # if base not in dict_max:
                #     dict_max[base] = i
                # else:
                #     dict_max[base] = max(i, dict_max[base])
                if dict_min[base] == -1:
                    dict_min[base] = i
                else:
                    dict_min[base] = min(i,dict_min[base])
                if dict_max[base] == -1:
                    dict_max[base] = i
                else:
                    dict_max[base] = max(i, dict_max[base])
            dict_min_re = []
            dict_max_re = []
            for i in range(N+1):
                # if(i == 0):
                #     res = dict_min[i+1] - dict_max[i]
                # else:
                # res = max(dict_min[i+1] - dict_max[i], res)
                if dict_min[i] != -1:
                    dict_max_re.append(dict_max[i])
                    dict_min_re.append(dict_min[i])
            for i in range(len(dict_max_re) - 1):
                if(i == 0):
                    res = dict_min_re[i + 1] - dict_max_re[i]
                else:
                    res = max(dict_min_re[i + 1] - dict_max_re[i], res)
        print('res ',res)
        return res


if __name__ == '__main__':
    # a = Test(14,602,5,[253, 14, 254, 212, 577])
    # a.max_gaptest()
    # a.maxgap()
    # a = Test(0, 1000, 20)
    # a.look()
    # a.max_gaptest()
    # a.maxgap()
#   对数器       Test
    for i in range(10000):
        mi = randint(0,36)
        ma = randint(50,999)
        num = randint(0,1000)
        a = Test(mi,ma,num)
        if(a.max_gaptest() - a.maxgap()) != 0:
            print("wrong!!!", mi,' ',ma,' ',num)
            print(a.list)
            break
    print('恭喜你通过所有验证*10000')
