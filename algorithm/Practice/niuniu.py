# (x, f, d, p) = [int(i) for i in input().split()]
# day = 0
# while f>0 and d>x:
#     f -= 1
#     if f<=0:
#         d -= p
#         f += 1
#     d -= x
#     day += 1
# print(day)
a = int(input())
for i in range(a):
    (day, one, two, three) = [int(i) for i in input().split()]
