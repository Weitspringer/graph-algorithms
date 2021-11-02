from collections import deque

def bfs(adjacency_list, node_key):
    # adjacency_list is of form {"a": [<keys>], "b": [<keys>], ...}
    b = {}
    q = deque()
    q.append(node_key)
    num = 1
    b.update({node_key: num})
    while q:
        current_key = q.pop()
        for i in adjacency_list[current_key]:
            if i not in b:
                num += 1
                q.append(i)
                b.update({i: num})
    return b

adj = {"a": ["b", "c"], "b": ["a","c","d"], "c": ["a", "b"], "d": ["b"]}
print(bfs(adj, "a"))