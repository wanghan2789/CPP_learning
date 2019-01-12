import functools


class BCSet:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.count = 1

    def is_same_set(self, set2):
        set1 = self
        stack1 = []
        stack2 = []
        while set1 != set1.parent:
            stack1.append(set1)
            set1 = set1.parent
        while stack1:
            current = stack1.pop(0)
            current.parent = set1
        while set2 != set2.parent:
            stack2.append(set2)
            set2 = set2.parent
        while stack2:
            current = stack2.pop(0)
            current.parent = set2
        return set1 == set2

    def union(self, set2):
        if not self.is_same_set(set2):
            current = self
            while current != current.parent:
                current = current.parent
            while set2 != set2.parent:
                set2 = set2.parent
            max_set = current if current.count >= set2.count else set2
            min_set = current if current.count < set2.count else set2
            max_set.count += min_set.count
            min_set.count = 0
            min_set.parent = max_set


N, M = [int(i) for i in input().split()]
data = []
for i in range(M):
    v1, v2, v3 = [int(j) for j in input().split()]
    data.append([v1, v2, v3])
data.sort(key=functools.cmp_to_key(lambda x, y: -1 if x[2] >= y[2] else 1))
flag = False
oppsite_list = [-1 for i in range(N)]
BCSet_list = [-1 for i in range(N)]
for i in data:
    v1, v2, v3 = i
    if oppsite_list[v1-1] < 0 and oppsite_list[v2-1] < 0:
        BCSet_list[v1 - 1] = BCSet(v1)
        BCSet_list[v2 - 1] = BCSet(v2)
        oppsite_list[v1 - 1] = v2
        oppsite_list[v2 - 1] = v1
        continue

    if oppsite_list[v1-1] < 0 or oppsite_list[v2-1] < 0:
        zero = v1 if oppsite_list[v1-1] < 0 else v2
        non_zero = v1 if oppsite_list[v1-1] >= 0 else v2
        BCSet_list[zero - 1] = BCSet(zero)
        oppsite_list[zero - 1] = non_zero
        BCSet_list[zero - 1].union(BCSet_list[oppsite_list[non_zero - 1] - 1])
        continue

    if oppsite_list[v1-1] > 0 and oppsite_list[v2-1] > 0:
        if BCSet_list[v1-1].is_same_set(BCSet_list[v2-1]):
            flag = True
            print(v3)
            break

        else:
            BCSet_list[v1 - 1].union(BCSet_list[oppsite_list[v2 - 1] - 1])
            BCSet_list[v2 - 1].union(BCSet_list[oppsite_list[v1 - 1] - 1])
            oppsite_list[v1 - 1] = v2
            oppsite_list[v2 - 1] = v1
            continue


if not flag:
    print(0)


