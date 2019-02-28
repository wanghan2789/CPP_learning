# all_in, cap = [int(i) for i in input().split()]
# nums = [int(i) for i in input().split()]
# # print(all_in, cap, nums)
# flag = 1
# nums = nums[::-1]
# derta = all_in % cap
# res = []
# if derta:
#     res = nums[0:derta][::-1]
#     nums = nums[derta:]
# count = all_in//cap
# if count:
#     while nums:
#         res += nums[0:cap][::-1]
#         nums = nums[cap:]
# for i in res:
#     print(i, end=' ')
# print()



n = int(input())
s = input()
st = [i for i in s]
count = int((n-1)/3)
level = int(count*2 + 1)
# st.sort()
# print(st)
for i in range(level):
    if i >= count:
        print(" "*count + str(st.pop(0)))
    else:
        print(' '*(i)+str(st.pop(0)) + " "*(2*count-1 -2*i)+str(st.pop(0)))

