from collections import deque


def simple_dfs(adjacency_list, node_key):
    """
    Performs a Depth First Search on a graph given as an adjacency list outgoing from a node.
    This node is specified by its appropriate key in the adjacency list.

    :adjacency_list: Dictionary of form {"a": [<keys>], "b": [<keys>], ...}
    :node_key: Starting point node of the graph. Corresponding key in the adjacency list
    :return: Returns array containing node keys reachable with DFS from the starting node as keys. 
             The values denote in which order the nodes were found
    """
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
