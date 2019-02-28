class Stack(object):
    def __init__(self, array):
        self.arr = array

    def swap(self, l, r):
        self.arr[l],self.arr[r] =\
            self.arr[r],self.arr[l]

    def insert(self, nodeindex):
        while self.arr[nodeindex] > self.arr[int((nodeindex - 1)/2)]:
            self.swap(nodeindex, int((nodeindex - 1)/2))
            nodeindex = int((nodeindex - 1)/2)
            # print(nodeindex)

    def construction(self, l=0, r=0):
        if r == 0:
            r = len(self.arr) - 1
        while l<=r:
            self.insert(l)
            l += 1

    def reconstuction(self, index, size=-2):
        if size == -2:
            size = len(self.arr)
        left = index * 2 + 1
        while left < size:
            largest = left + 1 \
                if left + 1 < size and self.arr[left+1]>self.arr[left] \
                else left
            if self.arr[largest] <= self.arr[index]:
                break
            self.swap(index,largest)
            index = largest
            left = index * 2 + 1

    def sort(self):
        self.construction()
        size = len(self.arr)
        while size>0:
            self.swap(0,size-1)
            self.reconstuction(index=0,size = size-1)
            size -= 1


#Test
p = [1,5,8,9,10,15,28,36,22,7,5,4,1]
Test = Stack(p)
print('arr ',Test.arr)
# Test.construction()
# print('mrs ',Test.arr)
# Test.arr[0] = 0
# Test.reconstuction(0)
# print('res ',Test.arr)
Test.sort()
print('sor ',Test.arr)


