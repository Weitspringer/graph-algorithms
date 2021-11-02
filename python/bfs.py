from queue import Queue

def bfs(adjacency_list, node_key):
    # adjacency_list is of form {"a": [<keys>], "b": [<keys>], ...}
    b = {}
    q = Queue()
    q.put(node_key)
    num = 1
    b.update({node_key: num})
    while not q.empty():
        current_key = q.get()
        for i in adjacency_list[current_key]:
            if i not in b:
                num += 1
                q.put(i)
                b.update({i: num})
    return b

adj = {"a": ["b", "c"], "b": ["c","d"], "c": [], "d": ["a"]}
print(bfs(adj, "a"))