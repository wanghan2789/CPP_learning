'''
class solve(object):
    def __init__(self,a,b,k):
        self.res = 0
        self.resa = ''
        self.resb = ''
        self.a = a
        self.b = b
        self.k = k

    def construction(self,n = 1,tmp = ''):
        a = self.a
        b = self.b
        k = self.k

        if(n > k):
            if (len(tmp) == k):
                add = 0
                for t in tmp:
                    add += int(t)
                if add == int(a) or add == int(b):
                    self.res += 1
            return
        self.construction(n + 1, tmp + str(a))
        self.construction(n + 1, tmp + str(b))



    def result(self):
        print(self.res)



(a,b,k) = input().split()
# print(a,b,k)
a = int(a)
b = int(b)
k = int(k)
malfoy = solve(a,b,k)
malfoy.construction()
malfoy.result()

'''

# class solve(object):
#     def __init__(self, arr):
#         self.arr = arr
#
#     def construction(self,k = 0):
#         tmp = 0
#
#         self.construction(k + 1, tmp + self.arr[k])
#         self.construction(k + 1, tmp - self.arr[k])
#         self.construction(k + 1, str(self.arr[k])+str(self.arr[k-1]))









