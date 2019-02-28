def trans(you_need, num):
    result = 0
    str_num = str(num)
    for i in range(len(str_num)):
        result += int(str_num[i]) * you_need **(len(str_num) -i -1)
    return result

#n = 0
read = []
while True:
    temp = input()
    if (temp == 'END'):
        break
    read.append(temp)

#print(read)

result = []
if(len(result) == 1):
    print('None')
else:
    for i in read:
        temp = i.split('#')
        you_need = int(temp[0])
        num = int(temp[1])
        transition = trans(you_need, num)
        # if transition not in result:
        #     result.append(transition)
        result.append(transition)
    n = 0
    sc = []
    for j in range(len(result)):
        if(result.count(result[j]) == 1):
            sc.append(read[j])
        else:
            continue

    if len(sc) == 0:
        print('None')
    else:
        for k in sc:
            print(k)




