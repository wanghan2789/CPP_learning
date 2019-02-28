class stack:
    def __init__(self, size=4):
        self.arr = [0 for x in range(size)]
        self.size = size
        self.index = 0

    def stack_insert(self, element):
        if self.index > self.size-1:
            return
        self.arr[self.index] = element
        self.index += 1

    def stack_pop(self):
        self.index = min(self.size-1,self.index)
        res = self.arr[self.index]
        self.index = max(self.index-1, 0)
        print(res)
        return res

    def look(self):
        print(self.arr)

#for Test
a = stack()
a.look()
print('----')
a.stack_insert(1)
a.stack_insert(2)
a.stack_insert(3)
a.stack_insert(4)
a.stack_insert(5)
print('----')
a.look()
print('----')
a.stack_pop()
a.stack_pop()
a.stack_pop()
a.stack_pop()
a.stack_pop()
print('----')
a.look()