class StackWi(object):
    def __init__(self):
        self.arr = []
        self.arr_min = []
        self.size = 0

    def stack_insert(self, element):
        if self.arr == []:
            self.arr.append(element)
            self.arr_min.append(element)
            self.size += 1
            return
        self.arr.append(element)
        self.arr_min.append(min(element,self.arr_min[self.size - 1]))
        self.size += 1

    def stack_pop(self):
        if self.arr == []:
            return
        res = self.arr.pop()
        res_m = self.arr_min.pop()
        print(res)
        self.size = max(self.size-1,0)
        return res

    def stack_popmin(self):
        res = self.arr.pop()
        res_m = self.arr_min.pop()
        print(res_m)
        self.size = max(self.size - 1, 0)
        return res_m

    def look(self):
        print(self.arr)
        print(self.arr_min)


a = StackWi()
a.stack_insert(4)
a.stack_insert(6)
a.stack_insert(7)
a.stack_insert(3)
a.stack_insert(2)
a.stack_insert(4)
a.stack_insert(0)
a.look()
a.stack_pop()
a.stack_popmin()
a.stack_popmin()
a.stack_popmin()
a.stack_popmin()
a.stack_popmin()
a.stack_pop()
a.stack_pop()
a.stack_pop()
a.stack_pop()
a.stack_pop()
