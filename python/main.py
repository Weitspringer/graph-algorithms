import src
from test.tests import TestBasicAlgorithms

if __name__ == "__main__":
    print("Running tests...")
    basic = TestBasicAlgorithms()
    basic.test_simple_bfs()
    basic.test_sssp_bfs()
