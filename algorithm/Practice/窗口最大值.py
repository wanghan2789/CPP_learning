# coding=utf-8


class WindowsMax(object):
    def __init__(self, arr):
        self.arr = arr
        self.max_queue = []
        self.L = 0
        self.R = 0

    def expand_window(self):
        if self.R == len(self.arr):
            return
        current = len(self.max_queue) - 1
        while current >= 0:
            if self.arr[self.max_queue[current]] <= self.arr[self.R]:
                self.max_queue.pop()
                current -= 1
            else:
                self.max_queue.append(self.R)
                break
        if not self.max_queue:
            self.max_queue.append(self.R)
        self.R += 1

    def del_window(self):
        if self.L == len(self.arr) or not self.max_queue:
            return
        while self.max_queue and self.max_queue[0]<=self.L:
            self.max_queue.pop(0)
        self.L += 1


if __name__ == '__main__':
    arr = [4,3,5,7,9,6,1,5,2]
    Test = WindowsMax(arr)
    for i in arr:
        Test.expand_window()
        print(Test.max_queue)
    print('--')
    for i in arr:
        Test.del_window()
        print(Test.max_queue, 'clear')
    Test.del_window()
    print(Test.max_queue, 'clear')
    print(Test.L)