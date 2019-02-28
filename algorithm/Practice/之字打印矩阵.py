import random


class ZhiPrint(object):
    def __init__(self, m=3,n=3):
        self.arr = [[random.randint(0,10) for j in range(n)] for i in range(m)]
        self.m = m
        self.n = n

    def print(self):
        print(self.arr)

    def special_print(self):
        current_rx = 0
        current_ry = 1
        current_lx = 1
        current_ly = 0
        flag = True
        print(self.arr[0][0],end=" ")
        while True:
            self.index_print(current_lx,current_ly,current_rx,current_ry,flag)
            flag = not flag
            if current_ry==current_ly and current_rx==current_lx:
                break
            if current_ry < self.n - 1:
                current_ry += 1
            else:
                current_rx += 1
            if current_lx < self.m - 1:
                current_lx += 1
            else:
                current_ly += 1

    def index_print(self,lx,ly,rx,ry,flag):
        if flag:
            while rx <= lx:
                print(self.arr[rx][ry],end=" ")
                rx += 1
                ry -= 1
            return
        else:
            while lx >= rx:
                print(self.arr[lx][ly], end=" ")
                lx -= 1
                ly += 1


if __name__ == '__main__':
    Test = ZhiPrint(3,4)
    Test.print()
    Test.special_print()