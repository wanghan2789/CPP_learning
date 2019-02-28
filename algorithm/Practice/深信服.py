n = int(input())
res = []
# lis = []
for i in range(n):
    context = input().split()
    k = int(context.pop()) - 1
    lis = [int(j) for j in context]
    # print(lis)
    while True:
        if k < 3:
            res.append(lis[k])
            break
        else:
            string = str(lis[0]+lis[1]+lis[2])
            for p in string:
                lis.append(int(p))
            lis = lis[-3:]
            k -= len(string)

for i in res:
    print(i)
