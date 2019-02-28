class Queue:
    def __init__(self, size=4):
        self.arr = [0 for i in range(size)]
        self.size = 0
        self.len = size
        self.start = 0
        self.end = 0

    def queue_insert(self,element):
        if self.size >= self.len:
            return
        self.arr[self.start] = element
        self.start += 1
        self.size += 1
        if self.start > self.len - 1:
            self.start = 0

    def queue_pop(self):
        if self.size <= 0:
            return
        res = self.arr[self.end]
        self.end += 1
        self.size += 1
        if self.end > self.len - 1:
            self.end = 0
        print(res)
        return res

    def look(self):
        print(self.arr)


a = Queue()
a.queue_insert('1')
a.queue_insert('2')
a.queue_insert('3')
a.queue_insert('4')
a.queue_insert('5')
print('------')
a.look()
print('------')
a.queue_pop()
a.queue_pop()
a.queue_pop()
a.queue_pop()
a.queue_pop()



