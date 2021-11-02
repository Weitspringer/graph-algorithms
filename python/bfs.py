from collections import deque

## TODO: Adjacency list
def bfs(adjacency_list, node_key):
    # adj_list = {"a": [], "b": [], ...}
    b = [0] * len(adjacency_list.node_key)
    q = deque()
    q.append(node_key)
    num = 1
    b[adjacency_list.keys().index(node_key)] = num
    while q:
        current_key = q.pop
        for i in adjacency_list.current_key:
            if b[i] == 0:
                num += 1
                q.append(i)
                b[i] = num
    return b