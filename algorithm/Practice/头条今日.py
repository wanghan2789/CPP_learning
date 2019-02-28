# command = input()
# if command == '':
#     print('')
# command = list(command)
# i = 0
# while command:
#     try:
#         if command[i] == 'o':
#             command.pop(i)
#             try:
#                 if i != 0:
#                     command.pop(i-1)
#                     i -= 1
#             except:
#                 pass
#
#         else:
#             i = i+1
#     except:
#         break
# # print(''.join(command))
# i = 0
# while command:
#     try:
#         if command[i] == 'i':
#             command.pop(i)
#             try:
#                 if i != 0:
#                     command.pop(i-1)
#                     i -= 1
#             except:
#                 pass
#
#         else:
#             i = i+1
#     except:
#         break
#
# print(''.join(command))
# def trans(allin):
#     res = []
#     i = 0
#     while allin:
#         try:
#             if allin[i].islower() and allin[i+1].isupper():
#                 res.append((''.join(allin[0:i+1])).lower())
#                 for j in range(i+1):
#                     allin.pop(0)
#                 i = 0
#         except:
#             res.append((''.join(allin)).lower())
#             break
#
#         try:
#             if i != 0 and allin[i].isupper() and allin[i+1].islower():
#                 res.append((''.join(allin[0:i])).lower())
#                 for j in range(i):
#                     allin.pop(0)
#                 i = 0
#         except:
#             res.append((''.join(allin)).lower())
#             break
#         i += 1
#
#
#     return '-'.join(res)
#
# n = int(input())
# res = []
# for i in range(n):
#     allin = input()
#     allin = list(allin)
#     res.append(trans(allin))
# for i in res:
#     print(i)


n = int(input())
ourin = []
for i in range(n):
    ourin.append(int(input()))
res = 0
while ourin:
    if len(ourin) > 2:
        tmp = ourin.copy()
        ourin.pop()
        ourin.pop(0)
        min_value = min(ourin)
        min_index = ourin.index(min_value) + 1
        ourin = tmp.copy()
    else:
        min_value = min(ourin)
        min_index = ourin.index(min_value)
    left = 1
    right = 1
    if min_index-1>=0:
        left = ourin[min_index-1]
    if min_index+1<len(ourin):
        right = ourin[min_index+1]
    res += left*right*min_value
    ourin.pop(min_index)
print(res)



