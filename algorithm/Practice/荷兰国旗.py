class netherland_flag(object):
    def __init__(self, arr):
        self.arr = arr

    def simple_flag(self, num):
        zone_left = -1
        l = 0
        while l < len(self.arr):
            if(self.arr[l] <= num):
                zone_left += 1
                self.arr[l],self.arr[zone_left] =\
                    self.arr[zone_left],self.arr[l]
            l += 1

    def flag_sort(self, num):
        zone_left = -1
        zone_right = len(self.arr)
        l = 0
        r = zone_right - 1
        while(l < zone_right):
            if (self.arr[l] < num):
                zone_left += 1
                self.arr[l], self.arr[zone_left] = \
                    self.arr[zone_left], self.arr[l]
                l += 1
            elif (self.arr[l] > num):
                zone_right -= 1
                self.arr[l], self.arr[zone_right] = \
                    self.arr[zone_right], self.arr[l]
            else:
                l += 1
            # r += 1


p = input()
p = p.split()
p = list(p)
p = [int(x) for x in p]
print(p)
end = len(p)

#Test1
# simple = netherland_flag(p)
# simple.simple_flag(3)
# print(simple.arr)

#Test2
flag = netherland_flag(p)
flag.flag_sort(5)
print(flag.arr)
