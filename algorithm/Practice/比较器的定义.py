import functools
from random import randint

# def cmp_1(x, y):
#     if x == y:
#         return 0
#     if x < y:
#         return -1
#     return 1
#
#
# def cmp_2(x, y):
#     if x[0] == y[0]:
#         return cmp_1(y[1], x[1])
#     return cmp_1(x[0], y[0])
#
# a = [1,2,3,4,5,6,8]
# a.sort(key=functools.cmp_to_key(cmp_2))
#
# print(a)



class Solve(object):
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def yours_cmp(self,x,y):
        if abs(x-self.target) < abs(y-self.target):
            return -1
        else:
            return 1

    def reconstruction(self):
        self.arr.sort(key=functools.cmp_to_key(self.yours_cmp))

a = [randint(-100,100) for x in range(30)]
tar = -66
print(a)
A =Solve(a,tar)
A.reconstruction()
print(A.arr)



