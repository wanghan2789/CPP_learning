# -*- coding:utf-8 -*-

class Hanoi:
    def __init__(self):
        self.arr = []
        self.n = 0
        self.left = []
        self.mid = []
        self.right = []
        self.location = []
        self.flag = False
        self.num = 0

    def chkStep(self, arr, n):
        self.arr = arr
        self.n = n
        self.process()
        if not self.flag:
            return -1
        return self.num

    def process(self):
        self.left = [i for i in range(self.n)]
        self.location = [1 for i in range(self.n)]
        self.process_function('1', '2', '3', self.n)

    def process_function(self, here, help, aim, level):
        if not self.flag:
            if level == 1:
                if here == '1':
                    tmp = self.left.pop(0)
                elif here == '2':
                    tmp = self.mid.pop(0)
                elif here == '3':
                    tmp = self.right.pop(0)
                if aim == '1':
                    self.left.insert(0,tmp)
                if aim == '2':
                    self.mid.insert(0,tmp)
                if aim == '3':
                    self.right.insert(0,tmp)
                #print('Node '+ str(tmp) + ' from ' + here + ' to '+ aim + ' and help is ' + help)
                if self.location == self.arr:
                    self.flag = True
                    return
                self.location[tmp] = int(aim)
                self.num += 1
                if self.location == self.arr:
                    self.flag = True
                    return
                # print(self.location)

            else:
                self.process_function(here, aim, help, level-1)
                self.process_function(here, help, aim, 1)
                self.process_function(help, here, aim, level - 1)


if __name__ == '__main__':
    Test = Hanoi()
    # Test.n = 2
    # Test.process()
    # print(Test.chkStep([3,3],2))
    print(Test.chkStep([3,3], 2))