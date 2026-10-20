"""Group tests: person 2's Alpha-Beta and T1 checks.

Other members can add their own TestCase classes to this file.
"""

import unittest

from data_cases import case
from search import solve


class TestPerson2(unittest.TestCase):
    def test_T1_false_tie(self):
        # Independent calculation: A = min(10, 12) = 10;
        # B = min(10, 2) = 2; R must choose A with value 10.
        # A value-only check would miss the incorrect result (10, B).
        for algorithm in ("minimax", "alphabeta"):
            with self.subTest(algorithm=algorithm):
                result = solve(case("T1"), algorithm=algorithm, order="LR")
                self.assertEqual(
                    (result["value"], result["action"]),
                    (10, "A"),
                )

    def test_T0_pruning_bounds_and_counts(self):
        # Hand trace: A returns 10, so B inherits alpha = 10.
        # B11 reads 4 and skips L10; B12 reads 3 and skips L12;
        # B then returns 4 and skips the whole B2 subtree.
        result = solve(case("T0"), algorithm="alphabeta", order="LR")

        self.assertEqual((result["value"], result["action"]), (10, "A"))
        self.assertEqual(result["pruned_roots"], ["L10", "L12", "B2"])
        self.assertEqual(
            result["leaf_order"],
            ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08",
             "L09", "L11"],
        )
        self.assertEqual(
            set(result["unvisited_nodes"]),
            {"L10", "L12", "B2", "B21", "B22", "L13", "L14", "L15", "L16"},
        )
        for node, expected_value in (("B11", 4), ("B12", 3), ("B", 4)):
            with self.subTest(node=node):
                returned = result["returns"][node]
                # UPPER means the true value is <= the returned value.
                self.assertEqual(returned["value"], expected_value)
                self.assertEqual(returned["bound"], "UPPER")

        # 12 internal nodes + 10 leaves = 22 visited nodes.
        expected_counts = {
            "visited": 22,
            "expanded": 12,
            "leaves": 10,
            "cutoffs": 3,
            "pruned_branches": 3,
            "max_depth": 4,
        }
        for field, expected in expected_counts.items():
            with self.subTest(statistic=field):
                self.assertEqual(result[field], expected)
        self.assertEqual(
            result["visited"], result["expanded"] + result["leaves"]
        )


if __name__ == "__main__":
    unittest.main()
