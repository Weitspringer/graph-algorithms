from collections import deque


def simple_bfs(adjacency_list, node_key):
    """
    Performs a Breath First Search on a graph given as an adjacency list outgoing from a node.
    This node is specified by its appropriate key in the adjacency list.

    :adjacency_list: Dictionary of form {"a": [<keys>], "b": [<keys>], ...}
    :node_key: Starting point node of the graph. Corresponding key in the adjacency list
    :return: Returns array containing node keys reachable with BFS from the starting node as keys. 
             The values denote in which order the nodes were found
    """
    assert (node_key in adjacency_list), "Specified node key not in adjacency list"
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


if __name__ == "__main__":
    adj_1 = {"a": ["b", "c"], "b": ["a", "c", "d"], "c": ["a", "b"], "d": ["b"]}
    print(simple_bfs(adj_1, "a"))
    adj_2 = {"a": ["b", "c", "d"], "b": ["e"], "c": ["f"], "d": [], "e": ["g"], "f": [], "g": []}
    print(simple_bfs(adj_2, "a"))