# import functools
# def pd(r1,r2):
#     if abs(r1)>abs(r2):
#         return 1
#     else:
#         return -1
#
# num = input()[1:-1]
# num = num.split(',')
# l = len(num)
# for i in range(l):
#     num[i] = int(num[i])
# target = int(input())
# our = [x-target for x in num]
# # print(our)
# our = sorted(our,key=lambda x: abs(x))
# i = 0
# res = our[0]+our[1]+our[2]
# while i+2<l:
#     if abs(res) > abs(our[i]+our[i+1]+our[i+2]):
#         res = our[i]+our[i+1]+our[i+2]
#     i += 1
# # print(res)
# print(res+3*target)

# s = input()
# i = input()
# l = []
# u = [0 for pp in range(len(s))]
# for k in range(len(s)):
#     if s[k] == i:
#         l.append(k)
#
# for k in range(len(s)):
#     our = abs(k-l[0])
#     for g in l:
#         if our > abs(k-g):
#             our = abs(k-g)
#     u[k] = our
#
#
# print(u)

read = input()
count = 0
s = list(read)
tmp = s[0]
for i in s:
    re = s.count(i)
    if count<re:
        count = re
        tmp = i

out = read.split(tmp)
outok = tmp*count + ''.join(out)
print(outok)


