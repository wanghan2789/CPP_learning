#首先是图的节点
class Node(object):
    def __init__(self, value = 0):
        self.value = value
        self.in_ = 0  #图的入度
        self.out_ = 0  #图的出度
        self.next = []  #图的next node 有N个
        self.edges = []  #图的边


class Edges(object):
    def __init__(self,weight=0, from_=None, to_=None):
        self.weight = weight  #你的权重
        self.from_ = from_  #应用Node去初始化
        self.to_ = to_  #应用Node去初始化


class Graph(object):
    def __init__(self):
        self.link = {}  #这里是编号和node的对应
        self.edges_sets = set()


class GraphGenerator(object):
    def __init__(self, matrix):
        #我们会创建一个图对象，并返回
        my_graph = Graph()
        for i in range(len(matrix)):
            my_weight = matrix[i][0]
            from_id = matrix[i][1]
            to_id = matrix[i][2]
            if from_id not in my_graph.link:
                my_graph.link[from_id] = Node(from_id)
            if to_id not in my_graph.link:
                my_graph.link[to_id] = Node(to_id)
            from_node = my_graph.link[from_id]
            to_node = my_graph.link[to_id]
            new_edges = Edges(my_weight, from_node, to_node)
            from_node.next.append(to_node)
            from_node.out_ += 1
            to_node.in_ += 1
            from_node.edges.append(new_edges)
            my_graph.edges_sets.add(new_edges)
        self.graph = my_graph  #保存图到对象中


class Travel(object):
    def bfs(self, head=None):
        #宽度优先的遍历规则, 离原本节点最近的先输出
        if not head:
            return
        now_lis = [head]
        now_set = set()
        while now_lis:
            current = now_lis.pop(0)
            print(current.value)
            for i in current.next:
                if i not in now_set:
                    now_set.add(i)
                    now_lis.append(i)

    def dfs(self, head=None):
        if not head:
            return
        my_stack = [head]
        my_set = set()
        while my_stack:
            current = my_stack.pop()
            print(current.value)
            for i in current.next:
                if i not in my_set:
                    my_set.add(i)
                    my_stack.append(i)


if __name__ == '__main__':
             #     1
             #    / \
             # 2   -    3
    # weight from to
    matrix = [[1,1,2],[1,2,3],[1,1,3],[1,2,3]]
    Test = GraphGenerator(matrix)
    solution = Travel()
    solution.bfs(Test.graph.link[1])
    solution.dfs(Test.graph.link[1])