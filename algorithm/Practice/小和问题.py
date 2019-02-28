# from array import array
# arr = array('l',())
#print(arr)
class small_sum(object):
    def __init__(self, arr):
        self.arr = arr

    def merg(self, l, mid ,r):
        help = []
        current_l = l
        current_r = mid+1
        result = 0
        while current_l <= mid and current_r <= r:
            if self.arr[current_l] < self.arr[current_r]:
                result += self.arr[current_l] * (r - current_r + 1)
                help.append(self.arr[current_l])
                current_l += 1
            else:
                help.append(self.arr[current_r])
                current_r += 1
        if current_l <= mid:
            help += self.arr[current_l:mid+1]
        if current_r <= r:
            help += self.arr[current_r:r+1]
        self.arr[l:r+1] = help
        return result

    def merg_sort(self, l, r):
        if(l == r):
            return 0
        mid = l + ((r - l) >> 1)
        print(l,r,mid)
        return self.merg_sort(l, mid) + \
               self.merg_sort(mid+1, r) + \
               self.merg(l, mid, r)

p = input()
p = p.split()
p = list(p)
p = [int(x) for x in p]
print(p)
end = len(p)
hezi = small_sum(p)
print(hezi.merg_sort(0,end - 1))
print(hezi.arr)


#
# def merg(left,right):
#     help = []
#     l = 0
#     r = 0
#     while l<len(left) and r<len(right):
#         if(left[l]<right[r]):
#             help.append(left[l])
#             l += 1
#         else:
#             help.append(right[r])
#             r += 1
#     help += left[l:]
#     help += right[r:]
#     return help
#
# def merg_sort(alist):
#     if(len(alist)<=1):
#         return alist
#     num = int(len(alist)/2)
#     left = merg_sort(alist[:num])
#     right = merg_sort(alist[num:])
#     return merg(left,right)
#
# pso = merg_sort(p)
# print(pso)




