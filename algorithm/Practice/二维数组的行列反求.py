from random import randint
class resolve(object):
    def __init__(self,arr):
        self.arr = arr

    def match(self,row,col):
        try:
            if len(self.arr) == row and col == len(self.arr[0]):
                return True
        except:

            return False
        return False


if __name__ == '__main__':
    for i in range(10000):
        row = randint(0,1000)
        col = randint(0,1000)
        arr = [[0 for i in range(col)] for j in range(row)]
        a = resolve(arr)
        if not a.match(row,col):
            print('Fuck Error')
            print(row,col)

