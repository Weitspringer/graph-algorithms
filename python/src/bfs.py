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


def sssp_bfs(adjacency_list, node_key):
    """
    Computes solution for Single Source Shortest Path problem (SSSP) on an undirected graph given as an adjacency list outgoing from a node.
    This source node is specified by its appropriate key in the adjacency list.

    :adjacency_list: Dictionary of form {"a": [<keys>], "b": [<keys>], ...}
    :node_key: Source node from which shortest path to every other node is computed. Corresponding key in the adjacency list
    :return: Returns a dictionary 'layers' which contains the information in which layer each node resides. 
             Returns a dictionary 'pre' which contains the predecessor of each node on the shortest path
    """
    layers = {}
    marks = {}
    pre = {}
    q = Queue()
    q.put(node_key)
    marks.update({node_key: 1})
    layers.update({node_key: 0})
    while not q.empty():
        current_key = q.get()
        for i in adjacency_list[current_key]:
            if i not in marks:
                marks.update({i: 1})
                pre.update({i: current_key})
                layers.update({i: layers[current_key] + 1})
                q.put(i)
        marks.update({current_key: 2})
    return layers, pre