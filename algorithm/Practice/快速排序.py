from random import randint
class Quicksort(object):
    def __init__(self, arr):
        self.arr = arr

    def swap(self, l, r):
        self.arr[l],self.arr[r] =\
            self.arr[r],self.arr[l]

    def sort(self, l, r):
        if(r<=l):
            return None
        lmin = l
        rmax = r
        index = randint(l, r)
        num = self.arr[index]
        current_l = l - 1
        current_r = r + 1
        while l<current_r:
            if self.arr[l]<num:
                current_l += 1
                self.swap(l, current_l)
                l += 1

            elif self.arr[l] > num:
                current_r -= 1
                self.swap(l, current_r)
            else:
                l += 1
        self.sort(lmin, current_l)
        self.sort(current_r,rmax)

p = [1,5,8,9,10,15,28,36,22,7,5,4,1]
Test = Quicksort(p)
print('inp ',Test.arr)
Test.sort(0,len(p)-1)
print('sor ',Test.arr)

