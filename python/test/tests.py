import unittest
from src.bfs import simple_bfs, sssp_bfs
from src.dfs import simple_dfs


adj_1 = {"a": ["b", "c"], "b": ["a", "c", "d"], "c": ["a", "b"], "d": ["b"]} # same as undirected graph
adj_2 = {"a": ["b", "c", "d"], "b": ["a", "e"], "c": ["a", "f"], "d": ["a"], "e": ["b", "g"], "f": ["c"], "g": ["e"]}

class TestBasicAlgorithms(unittest.TestCase):

    def test_simple_bfs(self):
        print("Testing simple bfs...")
        print("Adjacency matrix: {}".format(adj_1))
        b_1_a = simple_bfs(adj_1, "a")
        print("Simple BFS from a: {}".format(b_1_a))
        b_1_b = simple_bfs(adj_1, "b")
        print("Simple BFS from b: {}".format(b_1_b))
        b_1_c = simple_bfs(adj_1, "c")
        print("Simple BFS from c: {}".format(b_1_c))
        b_1_d = simple_bfs(adj_1, "d")
        print("Simple BFS from d: {}".format(b_1_d))
        self.assertTrue(b_1_a["a"] == 1 and b_1_b["b"] == 1 and b_1_c["c"] == 1 and b_1_d["d"] == 1)
        self.assertLess(b_1_a["a"], b_1_a["b"])
        self.assertLess(b_1_a["a"], b_1_a["c"])
        self.assertLess(b_1_a["b"], b_1_a["d"])
        self.assertLess(b_1_a["c"], b_1_a["d"])
        self.assertEqual(b_1_a["d"], max(b_1_a.values()))
        print("Tests for simple BFS passed!")

    def test_simple_dfs(self):
        return

    def test_sssp_bfs(self):
        print("Testing BFS for single source shortest path problem...")
        l, p = sssp_bfs(adj_2, "a")
        print("Adjacency matrix: {}".format(adj_2))
        print("Source node: a")
        print("Layers: {}".format(l))
        self.assertTrue(l["a"] == 0 and l["b"] == l["c"] == l["d"] == 1 and l["e"] == l["f"] == 2 and l["g"] == 3)
        print("Predecessors: {}".format(p))
        self.assertEqual(p, {'b': 'a', 'c': 'a', 'd': 'a', 'e': 'b', 'f': 'c', 'g': 'e'})
        print("All tests passed!")
