from queue import Queue


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