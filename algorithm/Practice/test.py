for i in Coor_Ions:
    x = i[0]
    y = i[1]
    z = i[2]



a = []

for i in range(3):
    b = [int(i) for i in input().split()]
    a.append(b)
print(a)


# p = input()
# p = p.split()
# p = list(p)
# p = [int(x) for x in p]
# print(p)
# end = len(p)
# while end > 1:
#     for i in range(end -1):
#         if(p[i] > p[i+1]):
#             p[i],p[i+1] = p[i+1],p[i]
#     end = end - 1
# print(p)

#插入排序
# for i in range(1,end):
#     index = i
#     j = i
#     while j > 0:
#         if(p[j]<p[j-1]):
#             p[j],p[j - 1] = p[j-1],p[j]
#             j = j-1
#         else:
#             break
# print(p)

#归并排序


''''/*BUG*/
def merg(p,left,mid,right):
    current_l = left
    current_r = mid+1
    help = []
    while current_l<=mid and current_r<=right:
        if(p[current_l]<p[current_r]):
            help.append(p[current_l])
            current_l += 1
        else:
            help.append(p[current_r])
            current_r += 1
    #help += p[current_r:mid+1]
    if current_l <= mid:
        help += p[current_r:mid+1]
    if current_r <=right:
        help += p[mid+1:current_r+1]
    p = help
    print(help)

def sort_merg(p,left,right):
    if(left == right):
        return
    # print(left,right)
    mid = int((right + left)/2)
    # print(mid)
    sort_merg(p,left,mid)
    sort_merg(p,mid+1,right)
    merg(p,left,mid,right)


sort_merg(p,0,len(p) - 1)
print(p)
'''





def merg(left,right):
    help = []
    l = 0
    r = 0
    while l<len(left) and r<len(right):
        if(left[l]<right[r]):
            help.append(left[l])
            l += 1
        else:
            help.append(right[r])
            r += 1
    help += left[l:]
    help += right[r:]
    return help

def merg_sort(alist):
    if(len(alist)<=1):
        return alist
    num = int(len(alist)/2)
    left = merg_sort(alist[:num])
    right = merg_sort(alist[num:])
    return merg(left,right)

pso = merg_sort(p)
print(pso)

