import unittest
from src.bfs import simple_bfs
from src.dfs import simple_dfs

class TestBasicAlgorithms(unittest.TestCase):

    def test_simple_bfs(self):
        adj_1 = {"a": ["b", "c"], "b": ["a", "c", "d"], "c": ["a", "b"], "d": ["b"]}
        b_1_a = simple_bfs(adj_1, "a")
        b_1_b = simple_bfs(adj_1, "b")
        b_1_c = simple_bfs(adj_1, "c")
        b_1_d = simple_bfs(adj_1, "d")
        self.assertTrue(b_1_a["a"] == 1 and b_1_b["b"] == 1 and b_1_c["c"] == 1 and b_1_d["d"] == 1)
        self.assertLess(b_1_a["a"], b_1_a["b"])
        self.assertLess(b_1_a["a"], b_1_a["c"])
        self.assertLess(b_1_a["b"], b_1_a["d"])
        self.assertLess(b_1_a["c"], b_1_a["d"])
        self.assertEqual(b_1_a["d"], max(b_1_a.values()))
        adj_2 = {"a": ["b", "c", "d"], "b": ["e"], "c": ["f"], "d": [], "e": ["g"], "f": [], "g": []}

    def test_simple_dfs(self):
        return
