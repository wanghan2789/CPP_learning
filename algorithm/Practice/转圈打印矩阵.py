#给定一个m*n的矩阵，其中的数值是随机生成的；
#你需要按照转圈的方式打印矩阵；
#思路，左上角与右下角设定为一个线框；
#789
#456
#123
#789632145

from random import randint
class CirclePrint(object):
    def __init__(self, arr, m, n):
        self.arr = arr
        self.m = m  #col m
        self.n = n  #raw n

    def print_cir(self):
        left_x = 0 #列
        left_y = self.n - 1 #行
        right_x = self.m - 1 #列
        right_y = 0 #行
        current_x = left_y
        current_y = left_x

        while left_y >= right_y:
            current_x = left_y
            current_y = left_x
            if left_x == right_x and left_y == left_y:
                print(self.arr[left_y][left_x],end=' ')
                break
            if left_y == right_y:
                while current_y <= right_x:
                    print(self.arr[current_x][current_y], end=' ')
                    current_y += 1
                break
            if left_x == right_x:
                while current_x >= right_y:
                    print(self.arr[current_x][current_y], end=' ')
                    current_x -= 1
                break


            while current_y < right_x:
                print(self.arr[current_x][current_y], end=' ')
                current_y += 1

            while current_x > right_y:
                print(self.arr[current_x][current_y], end=' ')
                current_x -= 1

            while current_y > left_x:
                print(self.arr[current_x][current_y], end=' ')
                current_y -= 1

            while current_x < left_y:
                print(self.arr[current_x][current_y], end=' ')
                current_x += 1
                
            left_x += 1
            left_y -= 1
            right_x -= 1
            right_y += 1

if __name__ == '__main__':
    mi = 0
    ma = 10
    # col = randint(1,10)
    # raw = randint(0,10)
    # # col = 0
    # # raw = 4
    # arr = [[randint(mi,ma) for i in range(col)] for x in range(raw)]
    # arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # Test = CirclePrint(arr, 4, 3)
    arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(arr)
    Test = CirclePrint(arr, 4, 4)
    Test = CirclePrint(arr,4,4)
    Test.print_cir()