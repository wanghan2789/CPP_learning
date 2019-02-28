# from math import fabs
# content = input()
# content = content.split()
# n = int(content.pop(0))
# deal = []
# for i in content:
#     deal.append(float(i))
# my = deal[0]
# for i in range(n):
#     for j in range(i,n):
#         if fabs(sum(deal[i:j+1])) < my:
#             my = sum(deal[i:j+1])
#             res = (i,j,my)
#
# print(res[0], res[1],'%.1f' % res[2])

string = input()
content1 = string.split(',')
content2 = content1[0].split()

yours_num = int(content2.pop(0))
print(content2,yours_num)

for i in range(len(content2)):
    a = 0
    try:
        tmp = int(content2[i])
    except:
        print(-1)
        break
    if yours_num == int(content2[i]):
        print(i)
        break
    if yours_num < int(content2[i]):
        print(-1)
        break


