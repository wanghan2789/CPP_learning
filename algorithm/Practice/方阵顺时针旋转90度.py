from random import randint

class TransMatrix(object):
    def __init__(self, n):
        self.n = n
        self.arr = [[randint(1,9) for x in range(n)] for i in range(n)]
        # self.arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # self.arr = [[1, 8, 2, 2], [8, 1, 5, 4], [1, 4, 5, 3], [2, 9, 9, 2]]

    def trans(self):
        left_x = 0
        left_y = 0
        right_x = self.n - 1
        right_y = self.n - 1

        while left_x < right_x:
            current_x = left_x
            current_y = left_y
            i = right_x - left_x
            k = 0
            while current_y + k < right_y:
                self.arr[current_x][current_y + k],self.arr[current_x + k][current_y + i] = self.arr[current_x + k][current_y + i],self.arr[current_x][current_y + k]
                self.arr[current_x][current_y + k],self.arr[current_x + i][current_y + i - k] = self.arr[current_x + i][current_y + i - k],self.arr[current_x][current_y + k]
                self.arr[current_x][current_y + k],self.arr[current_x + i - k][current_y] = self.arr[current_x + i - k][current_y],self.arr[current_x][current_y + k]
                k += 1
            left_x += 1
            left_y += 1
            right_x -= 1
            right_y -= 1

    def look(self):
        print(self.arr)


if __name__ == '__main__':
    Test = TransMatrix(6)
    Test.look()
    Test.trans()
    Test.look()