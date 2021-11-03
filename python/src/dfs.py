from collections import deque


def simple_dfs(adjacency_list, node_key):
    assert (node_key in adjacency_list), "Specified node key not in adjacency list"
    b = {}
    q = deque()
    q.append(node_key)
    num = 1
    while q:
        current_key = q.pop()
        if current_key not in b:
            b.update({current_key: num})
            num += 1
            for i in adjacency_list[current_key]:
                if i not in b:
                    q.append(i)
    return b


if __name__ == "__main__":
    adj = {"a": ["b", "c", "d"], "b": ["e"], "c": ["f"], "d": [], "e": ["g"], "f": [], "g": []}
    print(simple_dfs(adj, "a"))
