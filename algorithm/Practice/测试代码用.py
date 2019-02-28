# for i in range(1 , 10):
#     print(i) 1...10
#print([1,2,3,1,4,5] == [1,2,3,4,5])
# def test(p):
#     p[0] = p[1]
#     return
# l = [1,2]
# test(l)
# print(l)
# a= [0,1,2]
# print(a[99:100])
# print([x for x in range(10)])
# print('%.5f'% 1.0)
# a = [0,1,2,3,4,5]
# b = [9,9,9]
# a[0:3] = b
# print(1 if -1<0 else 0)
# l = 0
# r = 2
# while True:
#     mid = (l - r)>>1
#     mid += l
#     r = mid
#     print((l," ",r))
# from random import randint
# print(randint(0,0))
# j = 0
# # for i in range(1000):
# #     j += 1
# # print(j)
# from multiprocessing import Process
# import time
#
# i = 0
# def test():
#     i = 0
#     for j in range(1000):
#         i += 1
#
# p = Process(target=test)
# p.start()
# time.sleep(1)
# p.terminate()
# p.join()

# s = input()
# # s = s.split()
# # print(len(s[-1]))
# import functools
# def mycmp(a,b):
#     if int(str(a)[0]) < int(str(b)[0]):
#         return 1
#     return -1
#
#
# n = int(input())
# num_li = []
# for i in range(n):
#     num_li.append(int(input()))
# #print(num_li)
# num_li.sort(key=functools.cmp_to_key(mycmp))
#
# # length = len(num_li)
# # for i in range(length):
# #     for j in range(i,length):
# #         if int(str(num_li[i])[0]) < int(str(num_li[j])[0]):
# #             num_li[i],num_li[j] = num_li[j],num_li[i]
# s = ''
# for i in num_li:
#     s += str(i)
#
# print(s)

# s = input().split()[::-1]
# re = ''
# for i in range(len(s)):
#     re += s[i]
#     if(i<len(s)-1):
#         re += " "
# print(re)
#print(max([123,2]))

'''二维数组的初始化，列 * 行'''
# two = [[0 for x in range(4)] for i in range(3)]
# print(two)
# two[0][0] = 1
# two[1][1] = 1
# two[2][2] = 1
# print(two)

# print([].pop())
# a = True
# = not a
# print(a)
# print(a)
# a
# a = [0]
# print(len(a[0]))
# a = [5,4,3,2,1]
# a.sort()
# print(a)
# print(1 if 1>2 else 2)

#拷贝测试
# class A(object):
# #     def __init__(self):
# #         self.a = 0
# #     def seek(self):
# #         print(self.a)
# # q = A()
# # p = q
# # p.a = 1
# # p.seek()
# # q.seek()
# # print(p)
# # print(q)
# # print(p == q)
# while []:
# #     print('r')
# # print([])
# res = [[]]
# res[-1].append(0)
# print('Asd'[0].isupper())
# print('Asd'.lower())
# a = ['a','s','d']
# print('-'.join(a))
# print(a[0:1])
# a = ['a','s','d']
# b = a.copy()
# a.pop()
# print('assssd'.split('s'))
# a = (1,2)
# a = list(a)
# a = [1,2,3]
# print(a[0:1])
# n = 3
# for i in range(1,n):
#         print(i)
# if not 1:
#     print('asd'+'as')
#
# count = [ [0]*(2+1) for i in range(1+1) ]
# print(count)
# count = [0,0,1,2,5,7,7,7,8]
# count = list(filter(lambda x: count.count(x)==1,count))
# print(count)
ap = "asdd"
ap.replace(ap[3], 's')
print(ap)



