deal = []
order = []
for i in input():
    deal.append(i)
for i in input():
    order.append(i)
current = 0
normal_mode = True
j = 0
while j < len(order):
    i = order[j]
    j += 1
    if i == 'i' and normal_mode:
        normal_mode = False
        continue
    if i == 'e' and not normal_mode:
        normal_mode = True
        continue
    if normal_mode:
        if i == 'f':
            if j == len(order) - 1:
                continue
            i = order[j]
            j += 1
            current_tmp = current
            flag = True
            current += 1
            if current < len(deal) and deal[current] == i:
                flag = False
            while current < len(deal) and deal[current] != i:
                current += 1
                if deal[current] == i:
                    flag = False
                    break
            if flag:
                current = current_tmp
            continue
        if i == 'x':
            deal.pop(current)
            current = min(current, len(deal) - 1)
            continue
        if i == 'h':
            current -= 1
            current = max(0, current)
            continue
        if i == 'l':
            current += 1
            current = min(current, len(deal)-1)
            continue
    if not normal_mode:
        if i != 'e':
            deal.insert(current, i)
            current += 1

print(''.join(deal))



