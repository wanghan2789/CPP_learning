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


if __name__ == '__main__':
    my_test0 = BCSet(0)
    my_test1 = BCSet(1)
    my_test2 = BCSet(2)
    my_test3 = BCSet(3)
    my_test4 = BCSet(4)
    my_test5 = BCSet(5)

    #测试合并 0 2 4一组; 1 3 5一组
    print(my_test0.union(my_test2))
    print(my_test0.union(my_test4))

    print(my_test1.union(my_test3))
    print(my_test1.union(my_test5))

    print(my_test0.union(my_test0))
    print(my_test1.union(my_test1))
    print('---------------------')

    #测试查询
    print(my_test0.is_same_set(my_test0))
    print(my_test0.is_same_set(my_test1))
    print(my_test0.is_same_set(my_test2))
    print(my_test0.is_same_set(my_test3))
    print(my_test0.is_same_set(my_test4))
    print(my_test0.is_same_set(my_test5))
    print('---------------------')

    #大量合并与查询
    print(my_test0.union(my_test2))
    print(my_test0.is_same_set(my_test0))
    print(my_test0.is_same_set(my_test1))
    print(my_test0.is_same_set(my_test2))
    print(my_test0.is_same_set(my_test3))
    print(my_test0.is_same_set(my_test4))
    print(my_test0.is_same_set(my_test5))
    print('---------------------')

    print(my_test0.union(my_test1))
    print(my_test0.is_same_set(my_test0))
    print(my_test0.is_same_set(my_test1))
    print(my_test0.is_same_set(my_test2))
    print(my_test0.is_same_set(my_test3))
    print(my_test0.is_same_set(my_test4))
    print(my_test0.is_same_set(my_test5))
    print('-'*10+'検証終わり'+'-'*10)
