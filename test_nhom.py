import unittest
from data_cases import case, parameter_tree
from search import solve


class TestParameterAndPruning(unittest.TestCase):

    def test_t0_parameter(self):
        expected = {
            10: (10, 10),
            11: (11, 9),
            14: (12, 9),
        }

        for t, (value, ab_leaves) in expected.items():
            with self.subTest(t=t):
                tree = parameter_tree(t)

                mm = solve(tree, "minimax", "LR")
                ab = solve(tree, "alphabeta", "LR")

                self.assertEqual((mm["value"], mm["action"]), (value, "A"))
                self.assertEqual((ab["value"], ab["action"]), (value, "A"))
                self.assertEqual(ab["leaves"], ab_leaves)

    def test_t1_pruning_preserves_action(self):
        tree = case("T1")

        mm = solve(tree, "minimax", "LR")
        ab = solve(tree, "alphabeta", "LR")

        self.assertEqual((mm["value"], mm["action"]), (10, "A"))
        self.assertEqual((ab["value"], ab["action"]), (10, "A"))
        self.assertEqual(ab["leaf_order"], ["L01", "L02", "L03"])
        self.assertEqual(ab["unvisited_nodes"], ["L04"])
        self.assertEqual(ab["returns"]["B"]["bound"], "UPPER")


if __name__ == "__main__":
    unittest.main()