from random import randint
x = []
o_min = 0
o_max = 100000
for i in range(10):
    x.append(randint(o_min,o_max))
print(x)
burr = {}
for i in range(10):
    if x[i] not in burr.key:
        burr[x[i]] = 1
    else:
        burr[x[i]] += 1

x_cp = []
for i in range(o_min,o_max+1):
    if i in burr.keys():
        for j in range(0,burr[i]):
            x_cp.append(i)
print(x_cp)