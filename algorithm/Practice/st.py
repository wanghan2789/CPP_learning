# # import re
# # context = input()
# # context = context.lower()
# # # print(context)
# # # context.replace(',',' ')
# # # context.replace('!',' ')
# # # context.replace('',' ')
# # context = re.sub("[^a-z]", " ",context)
# # # print(context)
# # lis = context.split()
# # count = 0
# # result = []
# # for i in lis:
# #     if ' ' not in i:
# #         if lis.count(i) >= count:
# #             if lis.count(i) > count:
# #                 result = []
# #                 count = lis.count(i)
# #                 result.append(i)
# #             if lis.count(i) == count and i not in result:
# #                 result.append(i)
# # for i in result:
# #     print(i,end='')
# #
# # print()
# #
# context = input()
# n,m = int(context.split()[0]), int(context.split()[1])
# #print((n,m))
# context = input().split()
# price = [int(x) for x in context]
# #print(price)
# couple = []
# for i in range(m):
#     temp = input().split()
#     couple.append([int(temp[0]), int(temp[1])])
#
# #print(couple)
# help = []
# #j = 0
# index = [x for x in range(m)]
# for i in couple:
#     help.append([i[1]/i[0],j])
#     #j += 1
#
# for i in range(m):
#     for j in range(m - i):
#         if help[i] > help[j]:
#             index[i],index[j] = index[j],index[i]
#
#
#
#
import random
context = input()
M,A,R = int(context.split()[0]),int(context.split()[1]),int(context.split()[2])
# print((M,A,R))
#print('%.5f'% 1.0)
# print('%.5f'% M/R)
if M >= R:
    print('%.5f'% 1.0)
else:
    con = 0
    all = 350000
    for i in range(all):
        sum = 0
        while True:
            sum += random.randint(1, R)
            if(sum>=A):
                if(sum<=M):
                    con += 1
                break
    a = (con/all)
    a = ('%.4f0' % a)
    print(a)
    # print("%000"a)
    # print('%.5f'% a)


